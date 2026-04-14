"""
OpenWeather API client module for geocoding and air pollution data retrieval.
"""

import requests
from typing import Optional


def get_coordinates(location: str, api_key: str) -> Optional[tuple[float, float]]:
    """
    Get latitude and longitude coordinates for a given location using OpenWeather Geocoding API.
    
    Args:
        location: City name or location string to geocode
        api_key: OpenWeather API key
        
    Returns:
        Tuple of (latitude, longitude) if successful, None otherwise
    """
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": location,
        "limit": 1,
        "appid": api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if not data:
            print(f"Error: Location '{location}' not found. Please try a different location.")
            return None
        
        # Extract coordinates from first result
        lat = data[0].get("lat")
        lon = data[0].get("lon")
        
        # Validate coordinates exist
        if lat is None or lon is None:
            print("Error: Invalid response from geocoding API - missing coordinates.")
            return None
        
        # Validate coordinate ranges
        if not (-90 <= lat <= 90):
            print(f"Error: Invalid latitude value ({lat}). Must be between -90 and 90.")
            return None
        
        if not (-180 <= lon <= 180):
            print(f"Error: Invalid longitude value ({lon}). Must be between -180 and 180.")
            return None
        
        return (lat, lon)
        
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your internet connection and try again.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to OpenWeather API. Please check your internet connection.")
        return None
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your .env file.")
        else:
            print(f"Error: HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching coordinates: {e}")
        return None
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error: Failed to parse geocoding response: {e}")
        return None


def get_air_pollution(lat: float, lon: float, api_key: str) -> Optional[dict[str, float]]:
    """
    Get air pollution data for given coordinates using OpenWeather Air Pollution API.
    
    Args:
        lat: Latitude (-90 to 90)
        lon: Longitude (-180 to 180)
        api_key: OpenWeather API key
        
    Returns:
        Dictionary containing air quality metrics (AQI, CO, NO, NO2, O3, SO2, PM2.5, PM10)
        if successful, None otherwise
    """
    # Validate coordinates before making request
    if not (-90 <= lat <= 90):
        print(f"Error: Invalid latitude value ({lat}). Must be between -90 and 90.")
        return None
    
    if not (-180 <= lon <= 180):
        print(f"Error: Invalid longitude value ({lon}). Must be between -180 and 180.")
        return None
    
    url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract air quality data from response
        if "list" not in data or not data["list"]:
            print("Error: Invalid response from air pollution API - missing data.")
            return None
        
        aqi_data = data["list"][0]
        
        # Extract main AQI value
        aqi = aqi_data.get("main", {}).get("aqi")
        
        # Extract component pollutants
        components = aqi_data.get("components", {})
        
        if aqi is None or not components:
            print("Error: Invalid response from air pollution API - missing air quality metrics.")
            return None
        
        return {
            "aqi": aqi,
            "co": components.get("co", 0),
            "no": components.get("no", 0),
            "no2": components.get("no2", 0),
            "o3": components.get("o3", 0),
            "so2": components.get("so2", 0),
            "pm2_5": components.get("pm2_5", 0),
            "pm10": components.get("pm10", 0)
        }
        
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your internet connection and try again.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to OpenWeather API. Please check your internet connection.")
        return None
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your .env file.")
        else:
            print(f"Error: HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching air pollution data: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error: Failed to parse air pollution response: {e}")
        return None
