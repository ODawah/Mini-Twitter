import uuid
from database.sql_connector import connect
from utilities.hasher import encrypt
from utilities.validate import is_valid_email, is_valid_user_name, is_valid_uuid


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


def find_user_by_email(email):
    db = connect()
    if db is None:
        return None
    if not is_valid_email(email):
        return False
    command_handler = db.cursor()
    command_handler.execute("""SELECT * FROM USER WHERE email = :email""", {'email': email})
    got = command_handler.fetchone()
    return got


def find_user_by_uuid(uuid_str):
    db = connect()
    if db is None:
        return None
    if not is_valid_uuid(uuid_str):
        return False
    command_handler = db.cursor()
    command_handler.execute("""SELECT * FROM USER WHERE uuid = :uuid""", {'uuid': uuid_str})
    got = command_handler.fetchone()
    return got

def update_user_name(name, user_uuid) -> bool:
    db = connect()
    if db is None:
        return None
    if not is_valid_user_name(name) or not is_valid_uuid(user_uuid):
        return False
    command_handler = db.cursor()
    command_handler.execute("""UPDATE USER SET name = :name 
                            WHERE uuid = :uuid """,
                            {'name': name, 'uuid': user_uuid})
    if command_handler.rowcount != 1:
        return False
    else:
        return True
