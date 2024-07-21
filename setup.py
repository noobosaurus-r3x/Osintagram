import configparser
import os
from encryption_utils import encrypt_message, generate_key

def setup():
    config = configparser.ConfigParser(interpolation=None)
    session_id = input("Enter your Instagram session ID: ")

    generate_key()
    encrypted_session_id = encrypt_message(session_id)

    config['DEFAULT'] = {
        'SessionID': encrypted_session_id.decode()
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    
    print("Configuration saved successfully.")

if __name__ == '__main__':
    setup()
