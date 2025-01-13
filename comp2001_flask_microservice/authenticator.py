import requests

AUTH_URL = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"

def authenticate_user(email, password):
    credentials = {"email": email, "password": password}
    try:
        response = requests.post(AUTH_URL, json=credentials)
        if response.status_code == 200:
            return response.json()  # Authenticated successfully
        else:
            return None  # Authentication failed
    except requests.RequestException as e:
        print(f"Error connecting to Authenticator API: {e}")
        return None