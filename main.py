from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Example usage of an API key from .env
API_KEY = os.getenv("API_KEY")

def main():
    if API_KEY:
        print("API Key loaded successfully.")
    else:
        print("API Key not found. Please check your .env file.")


if __name__ == "__main__":
    main()
