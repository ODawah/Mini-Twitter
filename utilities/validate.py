from uuid import UUID
import re
import bcrypt


# validate_uuid: function takes a uuid string and make sure that it's valid
def is_valid_uuid(uuid_string):
    if uuid_string is None:
        return False
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        return False

    return str(val) == uuid_string


# function takes user entered string and the hashed string retrieved from database and return bool of matching
def is_valid_pass(pass_string, encrypted_str):
    pass_bytes = pass_string.encode('utf-8')
    result = bcrypt.checkpw(pass_bytes, encrypted_str)

    return result


def is_valid_user_name(name):
    if len(name) > 50 or name == "":
        return False
    else:
        return True


def is_valid_email(email_address):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    match = re.match(regex, email_address)

    return bool(match)


def is_valid_tweet_text(text):
    if len(text) > 280 or text == "":
        return False
    return True