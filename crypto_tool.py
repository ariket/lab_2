#!/usr/bin/env python
"""crypto_tool.py"""

import os
import argparse
from cryptography.fernet import Fernet


def load_key(key_file):
    """Load the encryption key from the key file"""
    try:
        with open(key_file, 'rb') as file:
            try:
                return Fernet(file.read())
            except ValueError:
                print("Something wrong with the encryption key.")
                return False
    except FileNotFoundError:
        print("Encryption Key not found.")
        return False


def encrypt_file(file_path, key_file):
    """Function to encrypt a file"""
    fernet = load_key(key_file)

    if fernet:
        # Read the file contents
        with open(file_path, 'rb') as file:
            original_data = file.read()

        # Encrypt the data
        encrypted_data = fernet.encrypt(original_data)

        # Write the encrypted data back to the file (or a new file)
        encrypted_file_path = file_path + '.encrypted'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f"File '{file_path}' encrypted and saved as '{encrypted_file_path}'.")


def decrypt_file(encrypted_file_path, key_file):
    """Function to decrypt an encrypted file"""
    fernet = load_key(key_file)

    if fernet:
        with open(encrypted_file_path, 'rb') as encrypted_file: # Read the encrypted file contents
            encrypted_data = encrypted_file.read()

        try:                                                # Decrypt the data
            decrypted_data = fernet.decrypt(encrypted_data)
        except Exception as e:
            print(f"Failed to decrypt file: {e}")
            return

        # Write the decrypted data back to the original file (removing the .encrypted suffix)
        original_file_path = encrypted_file_path.replace('.encrypted', '')
        with open(original_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f"File '{encrypted_file_path}' decrypted and restored as '{original_file_path}'.")


def main_crypto_tool():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using a symmetric key.")

    # Define arguments for encrypting and decrypting
    parser.add_argument(
        'action',
        choices=['encrypt', 'decrypt'],
        help="Specify whether to 'encrypt' or 'decrypt' a file."
    )
    parser.add_argument(
        'file',
        help="The path to the file you want to encrypt or decrypt."
    )
    parser.add_argument(
        '--key',
        required=True,
        help="The path to the key file (e.g., crypto_key.key)."
    )

    # Parse the arguments
    args = parser.parse_args()

    if not os.path.exists(args.key):
        print(f"{os.path.basename(__file__)}: error: '{args.key}' key file doesn't exist")
    elif not os.path.exists(args.file):
        print(f"{os.path.basename(__file__)}: error: '{args.file}' doesn't exist")
    else:
        # Perform encryption or decryption based on the action
        if args.action == 'encrypt':
            encrypt_file(args.file, args.key)
        elif args.action == 'decrypt':
            decrypt_file(args.file, args.key)


if __name__ == "__main__":
    main_crypto_tool()
