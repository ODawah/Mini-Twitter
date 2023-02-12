import sqlite3


# connect: function returns a connection object of the database
def connect():
    try:
        conn = sqlite3.connect("twitter.db")
        c = conn.cursor()
        # USERS TABLE
        c.execute("""CREATE TABLE IF NOT EXISTS USER (
            uuid CHAR(36) PRIMARY KEY,
            email VARCHAR(255) UNIQUE,
            name VARCHAR(70),
            password TEXT
            )
            """)

        # TWEETS TABLE
        c.execute("""CREATE TABLE IF NOT EXISTS TWEETS (
            uuid CHAR(36) PRIMARY KEY,
            tweet TEXT NOT NULL,
            is_reply BOOL,
            is_deleted BOOL,
            user_id CHAR(36) NOT NULL,
            FOREIGN KEY (user_id) REFERENCES USER(uuid)
            )
            """)
        return conn

    except Exception as e:
        print("Error: ", e)
        print("failed to connect")
        return None
