import psycopg2

from database import mydb as database
from constant import database_name
from constant import (password_vault_tab, authentication_tab)
from encrypt_tools import forge_secret_key, encrypt_vault, decrypt_vault
import pandas as pd


password_manager_db = database(database_name)
password_manager_db.connect()

print(password_manager_db.vault_exist('123'))

encryted_df = password_manager_db.user_vault('123123')
print(encryted_df)
decrypted_df = decrypt_vault('b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6', encryted_df)
print(decrypted_df)

# DOING ALL THE UPDATING

# encrypted_df = encrypt_vault('b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6', decrypted_df)
# print(df)
# df = decrypt_vault('b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6', df)
# print(df)
# print(df)
# password_manager_db.update_user_vault('123123', encryted_df)
# try:
#     # password_manager_db.insert(
#     #     password_vault_tab,
#     #     {'uid': '123123', 'acc_description': 'adsdadas',
#     #     'acc_username': 'adasddasd', 'acc_password': 'asdadadasdsa'})
#     password_manager_db.insert(
#         authentication_tab,
#         {'uid': '123123', 'salt': 'adsdadas',
#          'hash': 'adasddasd'})
# except psycopg2.Error as e:
#     print(e, end='')


# print(
#     # password_manager_db.select(
#     #     password_vault_tab,
#     #     ['uid', 'acc_description', 'acc_username', 'acc_password'])
#     password_manager_db.select(
#         authentication_tab,
#         ['uid', 'salt', 'hash']))
