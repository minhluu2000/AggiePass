if __name__ == '__main__':
    key = random_str_gen(32)
    print(key)
    password = 'Csc346Z@'
    new_key = key[0:-len(password)] + password
    print(new_key)

    clear = 'HelloAggie'
    print('Before encryption:', clear)
    aes = AESCipher(new_key)
    cipher = aes.encrypt(clear)
    aes2 = AESCipher(new_key)
    clear = aes2.decrypt(cipher)
    print('Encryption:', cipher)
    print('After decryption:', clear)