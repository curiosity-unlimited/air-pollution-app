import os
import requests
from dotenv import load_dotenv
from utils import validate_coordinates
from typing import Optional, Dict

# Load environment variables from .env file
load_dotenv()

# Example usage of an API key from .env
API_KEY = os.getenv("API_KEY")

def get_coordinates(location: str) -> Optional[Dict[str, float]]:
    """
    Fetch longitude and latitude for a given location using OpenWeather Geocoding API.

    Args:
        location (str): The name of the location (e.g., city name).

    Returns:
        Optional[Dict[str, float]]: A dictionary containing 'latitude' and 'longitude' if successful, otherwise None.
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
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]
            if validate_coordinates(latitude, longitude):
                return {
                    "latitude": latitude,
                    "longitude": longitude
                }
            else:
                print("Invalid coordinates received.")
                return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_air_pollution_data(latitude: float, longitude: float) -> Optional[Dict]:
    """
    Fetch air pollution data for given coordinates using OpenWeather Air Pollution API.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        Optional[Dict]: Air pollution data if successful, otherwise None.
    """
    if not API_KEY:
        print("API Key not found. Please check your .env file.")
        return None

    base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching air pollution data: {e}")
        return None