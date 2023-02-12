import uuid
from database.sql_connector import connect
from utilities.hasher import encrypt
from utilities.validate import is_valid_email,is_valid_user_name


# create_user: function takes user's class and add user to the database then return bool of success
def create_user(user):
    db = connect()
    if db is None:
        return None

    if not is_valid_user_name(user.name) or not is_valid_email(user.email):
        return None
    command_handler = db.cursor()
    user.uuid = str(uuid.uuid4())
    user.password = str(encrypt(user.password))
    if user.password == "":
        return None
    command_handler.execute("INSERT INTO USER (uuid,name, email, password) VALUES (?, ?, ?, ?)",
                            (user.uuid, user.name, user.email, user.password))
    db.commit()
    if command_handler.rowcount != 1:
        return None
    return user
