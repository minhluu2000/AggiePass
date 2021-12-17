"""This library contains all the functions needed to 
   set, update, and store authentication information."""

import pandas as pd

import encrypt_tools as enc
from database import mydb as database
from constant import database_name, authentication_tab, authentication_primary_key


def new_uid_pin_to_db(
        db: database, uid: str, salt: str, pin: str) -> bool:
    """
    This functon returns True if we successfully change
    the password data. Else returns False. Use 
    new_uid_to_db 
    """
    if (db.uid_exist(uid)):
        db.insert(
            authentication_tab,
            {'uid': uid, 'salt': salt, 'pin': pin})
        return True
    return False


def delete_uid(db: database, uid: str) -> bool:
    if (db.uid_exist(uid)):
        db.delete_row(authentication_tab, "{}='{}'".format(
            authentication_primary_key[0], uid))


def login(db: database, uid: str, pin: str) -> bool:
    if (db.uid_exist(uid)):
        salt = db.uid_pin_salt(uid)
        authenticate_hash = enc.pin_hash(pin, salt)
        return db.uid_pin_hash(uid) == authenticate_hash
    return False


if __name__ == '__main__':

    db = database(database_name)
    db.connect()

    print(login(db, '8436B32E', 'hello'))
