import configparser
import os
from encryption_utils import decrypt_message

def load_configuration():
    config = configparser.ConfigParser(interpolation=None)
    config_path = 'config.ini'
    if not os.path.exists(config_path):
        raise FileNotFoundError("Configuration file not found.")
    config.read(config_path)
    encrypted_session_id = config['DEFAULT']['SessionID'].encode()
    session_id = decrypt_message(encrypted_session_id)
    return session_id
