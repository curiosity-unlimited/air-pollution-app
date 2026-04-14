"""
Air Pollution App - Retrieve and display air quality data for any location.
"""

import os
from dotenv import load_dotenv
import api_client


def display_air_quality(location: str, lat: float, lon: float, data: dict[str, float]) -> None:
    """
    Display air quality data in a formatted, user-friendly way.
    
    Args:
        location: Location name
        lat: Latitude
        lon: Longitude
        data: Dictionary containing air quality metrics
    """
    # AQI quality levels
    aqi_levels = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor"
    }
    
    aqi = int(data["aqi"])
    aqi_description = aqi_levels.get(aqi, "Unknown")
    
    print("\n" + "=" * 60)
    print(f"Air Quality Data for {location}")
    print(f"Coordinates: {lat:.4f}°, {lon:.4f}°")
    print("=" * 60)
    print(f"\nAir Quality Index (AQI): {aqi} - {aqi_description}")
    print("\nPollutant Concentrations (μg/m³):")
    print(f"  CO (Carbon Monoxide):        {data['co']:.2f}")
    print(f"  NO (Nitrogen Monoxide):      {data['no']:.2f}")
    print(f"  NO₂ (Nitrogen Dioxide):      {data['no2']:.2f}")
    print(f"  O₃ (Ozone):                  {data['o3']:.2f}")
    print(f"  SO₂ (Sulfur Dioxide):        {data['so2']:.2f}")
    print(f"  PM2.5 (Fine Particles):      {data['pm2_5']:.2f}")
    print(f"  PM10 (Coarse Particles):     {data['pm10']:.2f}")
    print("=" * 60 + "\n")


def main() -> None:
    """
    Main application entry point.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        print("Error: API_KEY not found in .env file.")
        print("Please create a .env file with your OpenWeather API key.")
        print("See .env.example for reference.")
        return
    
    print("Welcome to the Air Pollution App!")
    print("-" * 60)
    
    # Get location from user
    location = input("Enter a location (city name): ").strip()
    
    if not location:
        print("Error: Location cannot be empty.")
        return
    
    # Get coordinates for the location
    print(f"\nFetching coordinates for '{location}'...")
    coordinates = api_client.get_coordinates(location, api_key)
    
    if coordinates is None:
        return
    
    lat, lon = coordinates
    print(f"Found: {lat:.4f}°, {lon:.4f}°")
    
    # Get air pollution data
    print("Fetching air quality data...")
    air_data = api_client.get_air_pollution(lat, lon, api_key)
    
    if air_data is None:
        return
    
    # Display results
    display_air_quality(location, lat, lon, air_data)


if __name__ == "__main__":
    main()
