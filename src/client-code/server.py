import mysql.connector
from mysql.connector import errorcode

def parseRequest(request):
    parts = request.split()
    print("Request parsed" + str(parts))
    response = "nice"
    try:
        cnx = mysql.connector.connect(host='marmoset04.shoshin.uwaterloo.ca',
                                    database='NHL_356')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
    return response