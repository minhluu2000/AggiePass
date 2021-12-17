# # Creating a new account
# # Connect to database
# db = database(database_name)
# db.connect()

# # Read tag to get UID, check if it is new
# rfid_card_data = arduino_wr(mode='r')
# uid = rfid_card_data[0]
# uid_status = db.uid_exist(uid)
# print(uid)
# if (not uid_status):
#     print('New UID detected...')
# else:
#     print('UID recognized! Please use log in screen instead!')
#     exit()

# # Generate a random string key
# rand_str = enc.random_str_gen()

# # Write it to rfid tag
# rfid_card_data = arduino_wr(mode='w', random_str=rand_str)
# written_rand_str = rfid_card_data[1]
# if rand_str == enc.hex_to_string(written_rand_str):
#     print('Successfully written to the card!')

# # Get a pin entry from user (Lide working on it)
# new_pin = 'RANDOM123'  # <-- placeholder

# # Generate a salt -> store it in DB
# rand_salt = enc.generate_pin_salt()

# # Forge the secret key and pass it to the password manager screen
# secret_key = enc.forge_secret_key(
#     tag_random_str=written_rand_str, pin=new_pin)

# if (not uid_status):
#     hash = enc.pin_hash(new_pin, rand_salt)
#     new_uid_to_db(db=db, uid=uid, salt=rand_salt, hash=hash)