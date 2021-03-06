import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import re

from mysql.connector.connection import MySQLConnection

Err = {
    "accdenied": "ERR: Access denied to the database, please try again!",
    "baddb": "ERR: Database does not exist, please try later!"
}

# Wrapper function for insert statement.
# This is to ensure code is easier to write and debug.
# The caller just needs to ensure the parameters are met
# and they can be fairly certain there will not be a syntax error in the query.
def insert(table, fields):
    insertQ = "INSERT INTO " + str(table)
    insertQ += " VALUES ('" + str(fields[0]) + "'"
    for i in range(1, len(fields)):
        insertQ += ", '" + str(fields[i]) + "'"
    insertQ += ");"
    
    return insertQ

# Wrapper function for join clause.
# This is to ensure code is easier to write and debug.
# The caller just needs to ensure the parameters are met
# and they can be fairly certain there will not be a syntax error in the query.
def join(table1, table2, onClause):
    return str(table1) + " INNER JOIN " + str(table2) + " ON " + str(onClause)

# Wrapper function for select statement.
# This is to ensure code is easier to write and debug.
# The caller just needs to ensure the parameters are met
# and they can be fairly certain there will not be a syntax error in the query.
def select(fields, table, condition = None, orderBy = None, limit = None, distinct = False, subQuery = False):

    # Fields
    selectQ = "SELECT "
    if distinct:
        selectQ += "DISTINCT "
    selectQ += str(fields[0])

    # If there is a list of fields
    for i in range(1, len(fields)):
        selectQ += ", " + str(fields[i])
    
    # From clause
    selectQ += " FROM ( " + str(table) + " )"

    # Where clause
    if condition is not None:
        selectQ += " WHERE " + str(condition)
    
    # Order by clause
    if orderBy is not None:
        selectQ += " ORDER BY " + str(orderBy)

    # Limit clause
    if limit is not None:
        selectQ += " LIMIT " + str(limit)
    
    if not subQuery:
        selectQ += ";"

    return selectQ

# Wrapper function for delete statement.
# This is to ensure code is easier to write and debug.
# The caller just needs to ensure the parameters are met
# and they can be fairly certain there will not be a syntax error in the query.
def delete(table, condition):
    deleteQ = "DELETE FROM " + str(table)
    deleteQ += " WHERE " + str(condition) + ";"

    return deleteQ

# Wrapper function for update statement.
# This is to ensure code is easier to write and debug.
# The caller just needs to ensure the parameters are met
# and they can be fairly certain there will not be a syntax error in the query.
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

# Builds a response object from the raw response received from the connection via SQL
# It takes in headings as an input since the raw reponse does not contain the column names or headings
# Response object format: {
#    "colName1": [col1row1Val, col1ro2Val, col1row3Val],
#    "colName2": [col2row1Val, col2ro2Val, col2row3Val],
#    "colName3": [col3row1Val, col3ro2Val, col3row3Val]
# }
def buildResponseObj(headings, rawResponse):
    response = {}
    # 
    for h in headings:
        response[h] = []

    # For each row in the response
    for row in rawResponse:
        # For each field in the rawResponse row
        for i in range(len(row)):
            colName = headings[i % len(headings)]
            response[colName].append(str(row[i]))

    return response

# Connects to database
# Sends error if could not connect
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

# Get query response for input query with expected headings
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
        response = buildResponseObj(headings, response)
    
    return response

# Helper function: Get title id of a input movie
def getMovieId(movieName, cnx: MySQLConnection):
    query = select(["imdb_title_id"], "Movies", "title = '" + str(movieName) + "'", None, None)
    response = getQueryResponse(cnx, query, ["imdb_title_id"], None)
    if "imdb_title_id" in response:
        return response["imdb_title_id"][0]

# Helper function: Get the last index of the Movies table in int format (without the "tt")
def getLastIndex(cnx: MySQLConnection):
    query = select(
        ["imdb_title_id"],
        "Movies",
        None,
        "Movies.imdb_title_id DESC",
        "1"
    )
    expectedHeadings = ["imdb_title_id"]
    response = getQueryResponse(cnx, query, expectedHeadings, None)
    return int(response["imdb_title_id"][0].replace("tt", ""))
    

def addMovieToMovies(parts, cnx: MySQLConnection):
    queryParams = []
    # fix title id add one from last entry
    queryParams.append("tt" + str(getLastIndex(cnx) + 1)) #id
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
    response = getQueryResponse(cnx, query, [
        "imdb_title_id",
        "title",
        "original_title",
        "year_of_release",
        "date_published",
        "duration",
        "country",
        "language",
        "director",
        "writer",
        "production_company",
        "actors",
        "description",
        "budget",
        "usa_gross_income",
        "worldwide_gross_income",
        "reviews_from_users",
        "reviews_from_critics"
    ], None)
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

def getMovieDetails(parts, cnx: MySQLConnection):

    # First, get the movie name
    movieName = str(parts[1])

    # Now, build query
    query = select([
            "title AS Title",
            "original_title AS 'Original Title'",
            "year_of_release AS Year",
            "date_published AS 'Date Published'",
            "duration AS Duration",
            "country AS Country",
            "language AS Language",
            "director AS 'Director(s)'",
            "writer AS 'Writer(s)'",
            "production_company AS 'Production Company'",
            "actors AS 'Actor(s)'",
            "description AS Description",
            "budget AS Budget",
            "usa_gross_income AS 'USA Gross Income'",
            "worlwide_gross_income AS 'Worldwide Gross Income'",
            "reviews_from_users AS 'Number of User Reviews'",
            "reviews_from_critics AS 'Number of Critic Reviews'"
        ],
        "Movies",
        "title = '" + str(movieName) + "'"
    )
    expectedHeadings = [
        "Title",
        "Original Title",
        "Year",
        "Date Published",
        "Duration",
        "Country",
        "Language",
        "Director(s)",
        "Writer(s)",
        "Production Company",
        "Actor(s)",
        "Description",
        "Budget",
        "USA Gross Income",
        "Worldwide Gross Income",
        "Number of User Reviews",
        "Number of Critic Reviews"
    ]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getTopNMovies(parts, cnx: MySQLConnection):

    # First get n
    n = int(parts[1])

    # Now, build query
    query = select(
        ["Movies.title AS Title", "Ratings.weighted_average_vote AS Rating", "Movies.language AS Language", "Movies.duration AS Duration"],
        join("Movies", "Ratings", "Movies.imdb_title_id = Ratings.imdb_title_id"),
        None,
        "Ratings.weighted_average_vote DESC",
        str(n)
    )
    expectedHeadings = ["Title", "Rating", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getActorsInMovies(parts, cnx: MySQLConnection):

    # First get the movie name
    movieName = str(parts[1])

    # Now, build query
    query = select(
        ['Actors.name AS "Actor Name"'],
        join("Movies", "Actors", "Movies.imdb_title_id = Actors.imdb_title_id"),
        "Movies.title = '" + str(movieName) + "'",
        None,
        None
    )
    expectedHeadings = ["Actor Name"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getTop10MoviesByGenre(parts, cnx: MySQLConnection):

    # First, get the genre and limit
    genre = str(parts[1])
    limit = str(parts[2])

    # Now, build the query
    query = select(
        ["T1.Name AS 'Name'", "Ratings.weighted_average_vote AS 'Rating'", "T1.Language AS Language", "T1.Duration AS Duration"],
        join("Ratings",
            "(" + select(
                ["Movies.title AS 'Name'", "Genres.genre AS 'genre'", "Movies.imdb_title_id AS 'imdb_title_id'", "Movies.language AS Language", "Movies.duration AS Duration"],
                join("Movies", "Genres", "Movies.imdb_title_id = Genres.imdb_title_id"),
                None,
                None,
                None,
                False,
                True
            ) + ") AS T1",
            "T1.imdb_title_id = Ratings.imdb_title_id"),
        "T1.genre like '%" + str(genre) + "%'",
        "Ratings.weighted_average_vote DESC",
        str(limit),
        True
    )
    expectedHeadings = ["Name", "Rating", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getActorsBornByDate(parts, cnx: MySQLConnection):

    # First, get the date

    # If parts[1] exists, request includes month-day format date.
    if len(parts) > 1:
        date = "-" + str(parts[1])
    # Else, use today's date
    else:
        date = datetime.today().strftime('-%m-%d')
    
    # Now, build the query
    query = select(
        ["Names.name AS Name"],
        join("Names", "MovieRoles", "Names.imdb_name_id = MovieRoles.imdb_name_id"),
        "(MovieRoles.played_role='actor' AND Names.date_of_birth like '%" + str(date) + "%')",
        None,
        None,
        True
    )
    expectedHeadings = ["Name"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getMostVotedNMoviesUS(parts, cnx: MySQLConnection):

    # First, get n
    n = int(parts[1])

    # Now, build query
    query = select(
        ["Movies.title AS Title", "Ratings.us_voters_votes AS Votes", "Movies.language AS Language", "Movies.duration AS Duration"],
        join("Movies", "Ratings", "Movies.imdb_title_id = Ratings.imdb_title_id"),
        None,
        "Ratings.us_voters_votes DESC",
        str(n)
    )
    expectedHeadings = ["Title", "Votes", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getMostVotedNMoviesOverall(parts, cnx: MySQLConnection):

    # First, get n
    n = int(parts[1])

    # Now, build query
    query = select(
        ["Movies.title AS Title", "Ratings.total_votes AS Votes", "Movies.language AS Language", "Movies.duration AS Duration"],
        join("Movies", "Ratings", "Movies.imdb_title_id = Ratings.imdb_title_id"),
        None,
        "Ratings.total_votes DESC",
        str(n)
    )
    expectedHeadings = ["Title", "Votes", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getTopMoviesFromX(parts, cnx):

    # First get the countryName
    countryName = str(parts[1])

    # Next, get the limit
    limit = str(parts[2])

    # Now, build the query
    query = select(
        ["Movies.title AS Title", "Ratings.weighted_average_vote AS Rating", "Movies.language AS Language", "Movies.duration AS Duration"],
        join("Movies", "Ratings", "Movies.imdb_title_id = Ratings.imdb_title_id"),
        "Movies.country LIKE '%" + str(countryName) + "%'",
        "Ratings.weighted_average_vote DESC",
        str(limit)
    )
    expectedHeadings = ["Title", "Rating", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getLowestRatedMovies(parts, cnx: MySQLConnection):

    # First, get the limit
    limit = str(parts[1])

    # Now, build the query
    query = select(
        ["Movies.title AS Title", "Ratings.weighted_average_vote AS Rating", "Movies.language AS Language", "Movies.duration AS Duration"],
        join("Movies", "Ratings", "Movies.imdb_title_id = Ratings.imdb_title_id"),
        None,
        "Ratings.weighted_average_vote",
        str(limit)
    )
    expectedHeadings = ["Title", "Rating", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getActedBetweenXandY(parts, cnx: MySQLConnection):

    # First get x and y years
    x = str(parts[1])
    y = str(parts[2])

     # Now, build the query
    query = select(
        ["Actors.name AS Name"],
        join("Movies", "Actors", "Movies.imdb_title_id = Actors.imdb_title_id"),
        "Movies.year_of_release BETWEEN " + str(x) + " AND " + str(y),
        None,
        None,
        True
    )
    expectedHeadings =["Name"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getMoviesByActor(parts, cnx: MySQLConnection):

    # First, get the actorName
    actorName = str(parts[1])

    # Now, build the query
    query = select(
        ["Movies.title AS Title", "Movies.language AS Language", "Movies.duration AS Duration"],
        join("Movies", "Actors", "Movies.imdb_title_id = Actors.imdb_title_id"),
        "Actors.name = '" + str(actorName) + "'"
    )
    expectedHeadings = ["Title", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getMoviesByDirector(parts, cnx: MySQLConnection):

    # First, get the directorName
    directorName = str(parts[1])

    # Now, build the query
    query = select(
        ["Movies.title AS Title", "Movies.language AS Language", "Movies.duration AS Duration"],
        join("Movies", "Directors", "Movies.imdb_title_id = Directors.imdb_title_id"),
        "Directors.name = '" + str(directorName) + "'"
    )
    expectedHeadings = ["Title", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getTopNMoviesOfYear(parts, cnx: MySQLConnection):

    # First, get n and year
    year = str(parts[1])
    n = str(parts[2])

    # Now, build the query
    query = select(
        ["Movies.title AS Title", "Ratings.weighted_average_vote AS Rating", "Movies.language AS Language", "Movies.duration AS Duration"],
        join("Movies", "Ratings", "Movies.imdb_title_id = Ratings.imdb_title_id"),
        "Movies.year_of_release = '" + str(year) + "'",
        "Ratings.weighted_average_vote DESC",
        str(n)
    )
    expectedHeadings = ["Title", "Rating", "Language", "Duration"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

def getActorsInXandY(parts, cnx: MySQLConnection):

    # First, get x and y movie names
    x = str(parts[1])
    y = str(parts[2])

    # Now, build the query
    query = select(
        ["Actors.name AS 'Name'"],
        join("Movies", "Actors", "Movies.imdb_title_id = Actors.imdb_title_id"),
        "Movies.title = '" + str(x) + "' AND Name IN (" + \
            select(
                ["Actors.name AS 'Name'"],
                join("Movies", "Actors", "Movies.imdb_title_id = Actors.imdb_title_id"),
                "Movies.title = '" + str(y) + "'",
                None,
                None,
                False,
                True
            ) + ")"
    )
    expectedHeadings = ["Name"]
    return getQueryResponse(cnx, query, expectedHeadings, None)

# This is the function the client calls and returns a response
def parseRequest(request):
    parts = request.split("$$")

    response, cnx = connectToDB()

    if response in Err:
        return response

    if parts[0] == "am":
        # Add movie with details in the other parts
        response = addMovieToMovies(parts, cnx)
    elif parts[0] == "dm":
        # Delete the movie data from all the related tables: Movies, Actors, etc.
        response = deleteMovieFromAllTables(parts, cnx)
    elif parts[0] == "um":
        response = updateMovieData(parts, cnx)
    elif parts[0] == "gmd":
        response = getMovieDetails(parts, cnx)
    elif parts[0] == "tm":
        response = getTopNMovies(parts, cnx)
    elif parts[0] == "actm":
        response = getActorsInMovies(parts, cnx)
    elif parts[0] == "tmg":
        response = getTop10MoviesByGenre(parts, cnx)
    elif parts[0] == "abt":
        response = getActorsBornByDate(parts, cnx)
    elif parts[0] == "mvus":
        response = getMostVotedNMoviesUS(parts, cnx)
    elif parts[0] == "mvo":
        response = getMostVotedNMoviesOverall(parts, cnx)
    elif parts[0] == "tmxc":
        response = getTopMoviesFromX(parts, cnx)
    elif parts[0] == "lrm":
        response = getLowestRatedMovies(parts, cnx)
    elif parts[0] == "awaxy":
        response = getActedBetweenXandY(parts, cnx)
    elif parts[0] == "mba":
        response = getMoviesByActor(parts, cnx)
    elif parts[0] == "mdd":
        response = getMoviesByDirector(parts, cnx)
    elif parts[0] == "tmy":
        response = getTopNMoviesOfYear(parts, cnx)
    elif parts[0] == "abmxy":
        response = getActorsInXandY(parts, cnx)

    return response