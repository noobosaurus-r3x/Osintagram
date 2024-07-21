# Osintagram

## Introduction
Osintagram is a command-line tool designed for conducting open-source intelligence (OSINT) gathering on Instagram profiles. It provides users with the ability to retrieve detailed information about Instagram users in a secure and efficient manner.

## Features
- **User Information Retrieval**: Easily fetch detailed information about Instagram users.
    - Retrieve user information including username, full name, verification status, follower count, following count, number of posts, biography, website, and more.
- **Secure Credential Storage**: Uses encryption to securely store user credentials.
- **Efficient Session Management**: Manages Instagram API sessions to enhance performance.
- **User-Friendly Interface**: Command-line interface for straightforward interaction.

## Prerequisites
- Python 3.6 or higher
- Pip for Python 3

## Installation
1. Clone the Osintagram repository:
    ```bash
    git clone https://github.com/noobosaurus-r3x/osintagram.git
    ```
2. Navigate to the Osintagram directory:
    ```bash
    cd osintagram
    ```
3. Install the required dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

## Initial Setup
Perform the initial setup to configure the tool with your Instagram session ID:
```bash
python3 osintagram.py --setup
```
Follow the prompt to enter your Instagram session ID. The session ID will be encrypted and saved securely in the configuration file.
Your Instagram session ID is you SessionID cookie, obviously.

## Usage
To fetch information about an Instagram user, use the following command:
```bash
python3 osintagram.py -u <target_username>
```
Replace `<target_username>` with the Instagram username of the person you are interested in.

## Configuration
- `config.ini`: Stores the encrypted session ID securely.
- `instagram_api_handler.py`: Handles interactions with the Instagram API.
- `output_manager.py`: Contains functions to format and display output.
- `setup.py`: Handles the initial setup to configure the tool.
- `encryption_utils.py`: Contains functions for encrypting and decrypting the session ID.

## File Overview
- `osintagram.py`: The main script that runs the tool and handles command-line arguments.
- `setup.py`: Script to handle initial setup and configuration.
- `environment_config.py`: Manages loading configuration securely.
- `instagram_api_handler.py`: Interacts with the Instagram API to fetch user information.
- `output_manager.py`: Formats and displays the fetched user information.
- `user_agent_manager.py`: Manages random user agent selection to mimic real browser requests.
- `config.ini`: Configuration file generated after running the setup.
- `secret.key`: File storing the encryption key generated during setup.

## Credits
Osintagram is inspired by Palenath's Toutatis. Special thanks to Palenath for the original creation. https://github.com/megadose/toutatis
