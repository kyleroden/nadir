#HW 5 - Encryption Program
#Kyle Roden
#CS 161

import string

def caeser():

    print("Welcome to the Caeser Cipher Program.")
    encrypt_choice = input("Enter 'e' to encrypt a file and 'd' to decrypt a file.")
    shift_num = input('Enter the shift value you would like to use, for example 1-10.')
    if encrypt_choice == 'e':
        #run the encryption
        encrypt(shift_num)
    elif encrypt_choice == 'd':
            #run the decryption
        decrypt(shift_num)
    else:
        print("Invalid entry.")


def encrypt(shift):
    try:
        encrypt_file = input("Enter the name of a file to encrypt. Or type quit to quit.")
        if encrypt_file.lower() != 'quit':
            output_file = input("Enter the name of the new encrypted file.")
            f = open(encrypt_file, 'r')
            w = open(output_file, 'w')
            lett = f.read(1)
            while lett != '':
                letter_num = ord(lett)
                if lett in string.ascii_uppercase:
                    #letter_num = ord(lett)
                    encrypt_letter_num = letter_num + int(shift)
                    if encrypt_letter_num > ord("Z"):
                        encrypt_letter_num -= 26
                        encrypt_letter = chr(encrypt_letter_num)
                        w.write(encrypt_letter)
                        lett = f.read(1)
                    else:
                        encrypt_letter = chr(encrypt_letter_num)
                        w.write(encrypt_letter)
                        lett = f.read(1)
                elif lett in string.ascii_lowercase:
                    encrypt_letter_num = letter_num + int(shift)
                    if encrypt_letter_num > ord('z'):
                        encrypt_letter_num -= 26
                        encrypt_letter = chr(encrypt_letter_num)
                        w.write(encrypt_letter)
                        lett = f.read(1)
                    else:
                        encrypt_letter = chr(encrypt_letter_num)
                        w.write(encrypt_letter)
                        lett = f.read(1)
                else:
                    w.write(lett)
                    lett = f.read(1)
            print("File encrypted. Goodbye.")
            return w
        else:
            print("Ok, farewell.")
    except FileNotFoundError:
        print("404 error. File not found.")

def decrypt(shift):
    try:
        #file_open = False
        decrypt_file = input("Enter the name of a file to decrypt. Or type quit to quit.")
        if decrypt_file.lower() != 'quit':
            output_file = input("Enter the name of the new unencrypted file.")
            f = open(decrypt_file, 'r')
            w = open(output_file, 'w')
            lett = f.read(1)
            while lett != '':
                letter_num = ord(lett)
                if lett in string.ascii_uppercase:
                    #letter_num = ord(lett)
                    decrypt_letter_num = letter_num - int(shift)
                    if decrypt_letter_num < ord("A"):
                        decrypt_letter_num += 26
                        decrypt_letter = chr(decrypt_letter_num)
                        w.write(decrypt_letter)
                        lett = f.read(1)
                    else:
                        decrypt_letter = chr(decrypt_letter_num)
                        w.write(decrypt_letter)
                        lett = f.read(1)
                elif lett in string.ascii_lowercase:
                    decrypt_letter_num = letter_num - int(shift)
                    if decrypt_letter_num < ord('a'):
                        decrypt_letter_num += 26
                        decrypt_letter = chr(decrypt_letter_num)
                        w.write(decrypt_letter)
                        lett = f.read(1)
                    else:
                        decrypt_letter = chr(decrypt_letter_num)
                        w.write(decrypt_letter)
                        lett = f.read(1)
                else:
                    w.write(lett)
                    lett = f.read(1)
            f.close()
            w.close()
            print("File decrypted. Goodbye.")
            return w
        else:
            print("Ok, farewell.")
    except FileNotFoundError:
        print("404 error. File not found.")
caeser()
