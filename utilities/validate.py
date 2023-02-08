from uuid import UUID
import bcrypt


# validate_uuid: function takes a uuid string and make sure that it's valid
def validate_uuid(uuid_string):
    if uuid_string is None:
        return False
    try:
        val = UUID(uuid_string,version=4)
    except ValueError:
            return False

    return str(val) == uuid_string

# validate_pass: function takes user enterd string and the hashed string retrieved from database and return bool of matching
def validate_pass(pass_string,encrypted_str):
    pass_bytes = pass_string.encode('utf-8')
    result = bcrypt.checkpw(pass_bytes,encrypted_str)
    
    return result
