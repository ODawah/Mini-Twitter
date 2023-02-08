import mysql.connector as mysql

# database connection variables
host = "localhost"
user = "root"
password = ""

# connect: function returns a connection object of the database
def connect():
    try:
        db = mysql.connect(host=host, user=user, password=password, database="twitter")
        return db
    except Exception as e:
        print("Error: ", e)
        print("failed to connect")
        return None
