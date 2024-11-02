#!/usr/bin/env python
"""laboration2.py"""
# This script is developed in Windows environment.
# Some testing done in Linux environment, seems to work ok.
# Author: Ari Ketola

# Assignment(in swedish):
#Skapa ett verktyg som kan:
#Generera och spara en krypteringsnyckel.
#Kryptera en fil med hjälp av en symmetrisk nyckel (filnamn som argument).
#Dekryptera en krypterad fil med rätt nyckel (filnamn som argument).

#Använd cryptography-biblioteket (Fernet rekommenderas)
#Använd argparse-biblioteket för att ta argument

#Krav:
    #Nyckelgenerering:
        #Skapa ett separat skript (ex: generate_key.py) som genererar
        # en symmetrisk nyckel och sparar den i en fil.

    #Kryptering och Dekryptering:
        #Implementera ett andra skript (ex crypto_tool.py) som använder
        # argparse för att hantera kommandoradsalternativ.
        # och utföra följande funktioner:
            #Kryptera en fil med en befintlig nyckel.
            #Dekryptera en krypterad fil och återställa originalet.
import os
import subprocess
import generate_key

EXIT_COMMAND = {"9", "x", "X", "z", "Z", "q", "Q"}

def main():
    """Main function"""
    def new_key():
        print("Are you sure you want to generate a new key in file", end =" ")
        print(f"'{generate_key.CRYPTO_KEY}'? (Y/N) \nThe old key will be overwritten.")
        while True:
            command = input(">>> ").lower()
            if command == "y":
                return generate_key.generate_key()
            if command == "n":
                break
            print(f"Invalid command: '{command}'.")
        return False

    def encrypt_file():
        print('Enter filename of the file you want to encrypt.')
        while True:
            file = input(">>> ")
            if os.path.exists(file):
                subprocess.run(["python", "crypto_tool.py", "encrypt", file,
                                "--key", generate_key.CRYPTO_KEY], check=False)
                break
            print("You must specify an existing file.")

    def decrypt_file():
        print('Enter filename of the file you want to decrypt.')
        while True:
            file = input(">>> ")
            if os.path.exists(file):
                subprocess.run(["python", "crypto_tool.py", "decrypt", file,
                                "--key", generate_key.CRYPTO_KEY], check=False)
                break
            print("You must specify an existing file that you want to decrypt.")

    def main_menu():
        print("**********Nmap Tool************************************")
        print("*  1 - Generate new key                               *")
        print("*  2 - Encrypt file                                   *")
        print("*  3 - Decrypt file                                   *")
        print("*  9 - Exit                                           *")
        print("*******************************************************")

    while True:
        main_menu()
        main_input = input(">>> ")
        if main_input == "1":
            new_key()
        elif main_input == "2":
            encrypt_file()
        elif main_input == "3":
            decrypt_file()
        elif main_input in EXIT_COMMAND:
            print("Crypto tool exiting...")
            break
        else:
            print(f"Invalid command: '{main_input}'.")

if __name__ == "__main__":
    main()
