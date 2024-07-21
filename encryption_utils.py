from cryptography.fernet import Fernet
import base64
import os

def generate_key():
    """Generate a key for encryption"""
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    """Load the previously generated key"""
    return open('secret.key', 'rb').read()

def encrypt_message(message):
    """Encrypts a message"""
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message):
    """Decrypts an encrypted message"""
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
