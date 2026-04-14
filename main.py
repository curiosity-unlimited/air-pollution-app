from dotenv import load_dotenv
import os
from api_requests import get_coordinates, get_air_pollution_data

# Load environment variables from .env file
load_dotenv()

# Example usage of an API key from .env
API_KEY = os.getenv("API_KEY")

def main():
    if API_KEY:
        print("API Key loaded successfully.")
    else:
        print("API Key not found. Please check your .env file.")

    location = input("Enter a location: ")
    coordinates = get_coordinates(location)

    if coordinates:
        print(f"Coordinates for {location}: {coordinates}")

        # Fetch air pollution data
        air_pollution_data = get_air_pollution_data(coordinates['latitude'], coordinates['longitude'])
        if air_pollution_data:
            print("Air Pollution Data:", air_pollution_data)
        else:
            print("Could not fetch air pollution data.")
    else:
        print("Could not fetch coordinates.")


if __name__ == "__main__":
    main()
