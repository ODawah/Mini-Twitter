import bcrypt

## This is the function that encrypts the passwords
def encrypt(password_str):
    if password_str == "" or password_str is None :
        return None
    # convert password to byte
    bytes = password_str.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes,salt)

    return hash
