import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Example usage of an API key from .env
API_KEY = os.getenv("API_KEY")

def get_coordinates(location):
    """
    Fetch longitude and latitude for a given location using OpenWeather Geocoding API.

    Args:
        location (str): The name of the location (e.g., city name).

    Returns:
        dict: A dictionary containing 'latitude' and 'longitude' if successful, otherwise None.
    """
    if not API_KEY:
        print("API Key not found. Please check your .env file.")
        return None

    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": location,
        "appid": API_KEY
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data:
            return {
                "latitude": data[0]["lat"],
                "longitude": data[0]["lon"]
            }
        else:
            print("No data found for the given location.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None