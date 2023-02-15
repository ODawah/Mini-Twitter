import uuid

from models.users import User
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
    user.password = encrypt(user.password)
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
        return None
    command_handler = db.cursor()
    command_handler.execute("""SELECT * FROM USER WHERE email = :email""", {'email': email})
    got_user = command_handler.fetchone()
    if got_user is None:
        return None
    result = User(uuid=got_user[0], email=got_user[1], name=got_user[2], password=got_user[3])
    return result


def find_user_by_uuid(uuid_str):
    db = connect()
    if db is None:
        return None
    if not is_valid_uuid(uuid_str):
        return None
    command_handler = db.cursor()
    command_handler.execute("""SELECT * FROM USER WHERE uuid = :uuid""", {'uuid': uuid_str})
    got_user = command_handler.fetchone()
    if got_user is None:
        return None
    result = User(uuid=got_user[0], email=got_user[1], name=got_user[2], password=got_user[3])
    return result


def update_user_name(name, user_uuid) -> bool:
    db = connect()
    if db is None:
        return False
    if not is_valid_user_name(name) or not is_valid_uuid(user_uuid):
        return False
    command_handler = db.cursor()
    command_handler.execute("""UPDATE USER SET name = :name
                            WHERE uuid = :uuid """,
                            {'name': name, 'uuid': user_uuid})
    db.commit()
    if command_handler.rowcount != 1:
        return False
    else:
        return True


def update_user_password(pass_str, user_uuid):
    db = connect()
    if db is None:
        return False
    if not is_valid_uuid(user_uuid) or pass_str == "":
        return False
    hashed_pass = encrypt(pass_str)
    command_handler = db.cursor()
    command_handler.execute("""UPDATE USER SET password = :pass 
                            WHERE uuid = :uuid """,
                            {'pass': hashed_pass, 'uuid': user_uuid})
    db.commit()
    if command_handler.rowcount != 1:
        return False
    else:
        return True


def delete_user(user_uuid):
    db = connect()
    if db is None:
        return False
    if not is_valid_uuid(user_uuid):
        return False
    command_handler = db.cursor()
    command_handler.execute("DELETE FROM USER WHERE uuid = :uuid ", {'uuid': user_uuid})
    db.commit()
    if command_handler.rowcount != 1:
        return False
    else:
        return True
