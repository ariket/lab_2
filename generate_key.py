#!/usr/bin/env python
"""generate_key.py"""
import os
from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

CRYPTO_KEY = 'crypto_key.key'           # File where key is stored


def generate_key():
    """Function to generate and save a symmetric key that can be used for encryption/decryption"""
    salt = os.urandom(16)               # Generate a random string "salt" of char using os.uradom()

    kdf = PBKDF2HMAC(                   # Deriving a key using PBKDF2HMAC
        algorithm=hashes.SHA256(),      # Using SHA-256 hashing algorithm
        length=32,                      # Generate a 256-bit key (32 bytes)
        salt=salt,                      # Use the generated salt
        iterations=480000,              # Number of iterations for key stretching
    )

    # Password to derive the key from
    password = b'my_secret_password'    # Replace this with a dynamic password input if needed

    # Deriving the key
    key = kdf.derive(password)
    encoded_key = urlsafe_b64encode(key)

    # Save the key to a file
    with open(CRYPTO_KEY, 'wb') as key_file:
        key_file.write(encoded_key)
    print(f"Key generated and saved to '{CRYPTO_KEY}' in '{os.getcwd()}\\'.")

if __name__ == "__main__":
    generate_key()
