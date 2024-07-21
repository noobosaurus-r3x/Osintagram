import requests
from user_agent_manager import select_random_user_agent

class InstagramAPIHandler:
    """Class to interact with Instagram's API using a session ID."""

    def __init__(self, session_id):
        """Initialize with session ID and setup session."""
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': select_random_user_agent(),
            'X-IG-App-ID': '936619743392459'
        }
        self.session.cookies.update({'sessionid': session_id})

    def fetch_user_information(self, username):
        """Fetch user information by username with comprehensive error handling."""
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json(), None
        except requests.exceptions.HTTPError as e:
            return None, f'HTTP Error: {e.response.status_code} - {e.response.reason}'
        except requests.exceptions.RequestException as e:
            return None, f'Request Error: {str(e)}'
        except ValueError:
            return None, 'JSON Decode Error'
