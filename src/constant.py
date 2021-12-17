"""This file contains all the basic credentials."""

# ===============DATABASE AUTHENTICATION===============
database_name = 'password_manager'
database_account = 'public_user'

# ===============DATABASE SCHEMA===============
password_vault_tab = 'password_vault' 
password_vault_col = ['uid', 'acc_description', 'acc_username', 'acc_password']
password_vault_col_typ = ['TEXT', 'TEXT', 'TEXT', 'TEXT']
password_vault_primary_key = ['uid']

authentication_tab = 'authentication'
authentication_col = ['uid', 'salt', 'pin_hash']
authentication_col_typ = ['TEXT', 'TEXT', 'TEXT']
authentication_primary_key = ['uid']
