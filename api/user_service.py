from db import get_connection

import hmac
import hashlib

from uuid import uuid4 as uuid

def create_user(email, password):
    #  hash password
    #  check if user exists and if not save 
    # return user
    con = get_connection()

    hashed_pw = hmac.new("secret".encode("UTF-8"), "password".encode(), hashlib.sha256).hexdigest()

    user_exists = con.execute("SELECT id from users where email=?", (email,))

    if user_exists.rowcount < 0:
        
        id = str(uuid())

        user = con.execute("""INSERT INTO users (id, email, hash) values (
                           ?,?,?
        )""", (id, email, password))
        return user
    else:
        raise Exception("User already exists")        

def login_user(email, hash_passowrd):
    # see if user exists with this email in db
    # if not return 404
    # compare hashes of passwords
    # if not equal return 403
    # then return user
    pass