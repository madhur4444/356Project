import mysql.connector
from mysql.connector import errorcode
import datetime

from mysql.connector.connection import MySQLConnection

Err = {
    "accdenied": "ERR: Access denied to the database, please try again!",
    "baddb": "ERR: Database does not exist, please try later!"
}

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
                                    database="NHL_356")
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

def parseRequest(request):
    parts = request.split()

    response, cnx = connectToDB()

    if response in Err:
        return response

    # query = ("SELECT * FROM Game LIMIT 5")
    # headings = ["gameID", "season", "gameType", "dateTimeGMT", "awayTeamID",
    #             "homeTeamID", "awayGoals", "homeGoals", "outcome", "homeRinkSideStart",
    #             "venue", "venueTimeZoneID", "venueTimeZoneOffset", "venueTimeZoneTZ"]
    # response = getQueryResponse(cnx, query, headings, None)

    if parts[0] == "am":
        # Add movie with details in the other parts
        print("Hello")
    elif parts[1] == "r":
        # Print movie ratings with parts[1] as the name of the movie
        print("Hello")

    return response