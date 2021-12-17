# Test
# acc_des = 'This is a test account.2'
# acc_username = '2'
# acc_password = '2'
# secret_msg = 'Hello :)'
# enc_acc_dess = enc.encrypt_data(
#     'b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6',
#     data=acc_des)
# enc_username = enc.encrypt_data(
#     'b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6',
#     data=acc_username)
# enc_acc_password = enc.encrypt_data(
#     'b2001bccdcb7ea5556526cb70e58206996c3039282dd62e2ddc4a1d55be6c1d6',
#     data=acc_password)

# # Test putting encrypted data to the database
# try:
#     db.insert(
#         password_vault_tab,
#         {'uid': '123123', 'acc_description': enc_acc_dess,
#         'acc_username': enc_username, 'acc_password': enc_acc_password})
# except psycopg2.Error as e:
#     print(e, end='')

# VERY DANGEROUS, DELETE EVERYTHING WITH THE SAME UID
# db.delete_row(password_vault_tab, condition='uid=\'{}\''.format('123123'))

# print('{}\n{}\n{}'.format(secret_msg, encrypted_msg, decrypted_msg))
# salt = enc.generate_pin_salt()