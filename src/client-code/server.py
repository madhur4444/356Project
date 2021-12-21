import mysql.connector
from mysql.connector import errorcode
import datetime
import random
import re

from mysql.connector.connection import MySQLConnection

Err = {
    "accdenied": "ERR: Access denied to the database, please try again!",
    "baddb": "ERR: Database does not exist, please try later!"
}

def insert(table, fields):
    insertQ = "INSERT INTO " + str(table)
    insertQ += " VALUES (%s"
    for i in range(len(fields) - 1):
        insertQ += ", %s"
    insertQ += ");"
    
    return insertQ

def select(table, fields, condition):
    selectQ = "SELECT " + str(fields[0])
    for i in range(1, len(fields)):
        selectQ += ", " + str(fields[i])
    selectQ += " FROM ( " + str(table) + " )"
    if condition is not None:
        selectQ += " " + str(condition)
    selectQ += ";"

    return selectQ

def delete(table, condition):
    deleteQ = "DELETE FROM ( " + str(table) + " )"
    deleteQ += " WHERE " + str(condition) + ";"

    return deleteQ

def update(table, fields, newVals, condition):
    updateQ = "UPDATE ( " + str(table) + " ) SET "
    updateQ += str(fields[0]) + " = '"  + str(newVals[0]) + "'"
    for i in range(1, len(fields)):
        field = fields[i]
        newVal = newVal[i]
        updateQ += ", "
        updateQ += str(field) + " = '"  + str(newVal) + "'"
    updateQ += " WHERE " + str(condition) + ";"

    return updateQ

def buildResponseObj(headings, rawResponse):
    response = {}
    for h in headings:
        response[h] = []

    # For each row in the response
    for row in rawResponse:
        # For each field in the rawResponse row
        for i in range(len(row)):
            colName = headings[i % len(headings)]
            response[colName].append(str(row[i]))

    return response

def connectToDB():
    response = ""
    try:
        cnx = mysql.connector.connect(host="marmoset04.shoshin.uwaterloo.ca",
                                    user="kjbhardw",
                                    password="loL_12345",
                                    database="db356_kjbhardw")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            response = Err["accdenied"]
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            response = Err["baddb"]
        else:
            print(err)
    return response, cnx

def getQueryResponse(conn: MySQLConnection, query, headings, queryParams):
    cursor = conn.cursor()
    if queryParams is None:
        cursor.execute(query)
    else:
        cursor.execute(query, queryParams)
    response = cursor.fetchall()

    if len(response) == 0:
        response = {"nodata": "true"}
    
    else:
        # print(response)
        response = buildResponseObj(headings, response)
    
    return response

def getMovieId(movieName, cnx: MySQLConnection):
    query = select("Movies", "imdb_title_id", "title = '" + str(movieName) + "'")
    response = getQueryResponse(cnx, query, ["imdb_title_id"], None)
    if "imdb_title_id" in response:
        return response["imdb_title_id"]

def addMovieToMovies(parts, cnx: MySQLConnection):
    queryParams = []
    queryParams.append("tt" + str(random.randint(9915000, 9999999))) #id
    queryParams.append(str(parts[1])) # title
    queryParams.append(str(parts[1])) # original title
    # queryParams.append(parts[2]) # year
    m = re.match('[0-9][0-9][0-9][0-9]', parts[2])
    if m:
        m = m.group(0)
        queryParams.append(m)
    else:
        queryParams.append("")
    queryParams.append(parts[2]) # date published
    for i in range(3, len(parts)):
        queryParams.append(str(parts[i]))
    query = insert("Movies", queryParams)
    print(len(queryParams))
    print(query)
    response = getQueryResponse(cnx, query, [], queryParams)
    return 'nodata' in response

def deleteMovieFromAllTables(parts, cnx: MySQLConnection):

    # First get the movie id
    movieId = getMovieId(parts[1], cnx)

    # Now, first delete from Movies using movieId
    query = delete("Movies", "imdb_title_id = '" + str(movieId) + "'")
    response = getQueryResponse(cnx, query, [], None)
    
    # Now, delete from all tables that have movieId: Ratings, MovieRoles, Genres
    query = delete("Ratings", "imdb_title_id = '" + str(movieId) + "'")
    response = getQueryResponse(cnx, query, [], None)

    query = delete("MovieRoles", "imdb_title_id = '" + str(movieId) + "'")
    response = getQueryResponse(cnx, query, [], None)

    query = delete("Genres", "imdb_title_id = '" + str(movieId) + "'")
    response = getQueryResponse(cnx, query, [], None)
    return 'nodata' in response

def updateMovieData(parts, cnx: MySQLConnection):

    # First, get movieId
    movieId = getMovieId(parts[1], cnx)

    # Now, for each other part of the given request, update that field to the newValue
    fields, newValues = [], []
    for i in range(2, len(parts)):
        updationSubReq = parts[i].split("?=")
        field, newValue = updationSubReq[0], updationSubReq[1]
        fields.append(field)
        newValues.append(newValue)
    
    query = update("Movies", fields, newValues, "imdb_title_id = '" + str(movieId) + "'")
    response = getQueryResponse(cnx, query, [], None)
    return 'nodata' in response


def parseRequest(request):
    parts = request.split("$$")

    response, cnx = connectToDB()

    if response in Err:
        return response

    if parts[0] == "am":
        # Add movie with details in the other parts
        response = addMovieToMovies(parts, cnx)
    elif parts[0] == "bm":
        # Delete the movie data from all the related tables: Movies, Actors, etc.
        response = deleteMovieFromAllTables(parts, cnx)
    elif parts[0] == "um":
        response = updateMovieData(parts, cnx)

    return response