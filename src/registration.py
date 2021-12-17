"""
This file contains all the functions needed for
new user registration.

Registration process:
- Create a new user id (read UID)-> store to authentication database
- Generate a random string key
- Write to rfid tag
- User create a custom pin
- Generate a random salt -> store to authentication database
- Once registration done -> forge the aes key and send the user
  to the password management screen.
"""

from database import mydb as database
from constant import authentication_tab

# Current UID function for reading, will be changed in the future


def new_uid_to_db(
        db: database, uid: str, salt: str, hash: str) -> bool:
    """
    This functon returns True if we successfully add the
    new user into the database. Else returns False.
    """
    if (not db.uid_exist(uid)):
        db.insert(
            authentication_tab,
            {'uid': uid, 'salt': salt, 'pin_hash': hash})
        return True
    return False


if __name__ == '__main__':
    pass
    