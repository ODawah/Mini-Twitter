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

db = mysql.connect(host=host, user=user, password=password, database="twitter")
command_handler = db.cursor()

try:
    command_handler.execute("SHOW DATABASES")
    for database in command_handler:
        print(database)
except Exception as e:
    print("Error: ", e)
    print("couldn't show all databases")

#USERS TABLE
command_handler.execute("CREATE TABLE IF NOT EXISTS USER (uuid CHAR(36) PRIMARY KEY, name VARCHAR(70), passwords TEXT)")
db.commit()

#TWEETS TABLE
command_handler.execute("CREATE TABLE IF NOT EXISTS TWEETS (uuid CHAR(36) PRIMARY KEY,tweet TEXT NOT NULL,is_reply BOOL,is_deleted  BOOL,user_id CHAR(36) NOT NULL,FOREIGN KEY (user_id) REFERENCES USER(uuid))")
db.commit()

command_handler.execute("SHOW TABLES")
for database in command_handler:
    print(database)
