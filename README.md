# Air Pollution App

An educational CLI application that retrieves and displays real-time air pollution data for locations around the world using the OpenWeather API.

## Features

✨ **Current Implementation:**
- 🌍 **Location-based Air Quality Lookup** — Enter any city name to get current air pollution data
- 📍 **Geocoding Integration** — Automatically converts location names to coordinates using OpenWeather Geocoding API
- 💨 **Comprehensive Air Quality Metrics** — Displays AQI and all major pollutants:
  - Air Quality Index (AQI) with descriptive levels (Good, Fair, Moderate, Poor, Very Poor)
  - Carbon Monoxide (CO)
  - Nitrogen Monoxide (NO)
  - Nitrogen Dioxide (NO₂)
  - Ozone (O₃)
  - Sulfur Dioxide (SO₂)
  - Fine Particles (PM2.5)
  - Coarse Particles (PM10)
- 🔒 **Secure API Key Management** — Uses `.env` file for safe credential storage
- ✅ **Input Validation** — Validates coordinates and API responses
- 🎯 **Modular Architecture** — Separate modules for API client logic and UI
- 📝 **PEP 484 Type Hints** — Full type annotations for better code quality and IDE support
- 🛡️ **Comprehensive Error Handling** — User-friendly error messages for network issues, invalid locations, and API errors

**Demo Branches:**
- `demo/agent-mode` — Compare your progress when working with Agent mode
- `demo/plan-agent-mode` — Compare your progress when working with Plan/Agent mode

## Project Structure

```
air-pollution-app/
├── main.py              # Main application entry point and user interface
├── api_client.py        # OpenWeather API client functions
├── pyproject.toml       # Project dependencies and metadata
├── .env                 # API key storage (not committed to git)
├── .env.example         # Template for required environment variables
├── .gitignore           # Git ignore rules (includes .env)
└── README.md            # This file
```

**Module Breakdown:**
- **`main.py`** — Handles user input, orchestrates API calls, and displays formatted results
- **`api_client.py`** — Contains `get_coordinates()` and `get_air_pollution()` functions with complete error handling

## Setup Instructions

### Prerequisites
- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- OpenWeather API key (free tier available)

### 1. Get Your OpenWeather API Key

1. Sign up for a free account at [OpenWeather](https://home.openweathermap.org/users/sign_up)
2. Navigate to your [API keys section](https://home.openweathermap.org/api_keys)
3. Copy your API key (it may take a few minutes to activate)

### 2. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/air-pollution-app
cd air-pollution-app

# Create .env file from template
cp .env.example .env

# Edit .env and add your API key
# Replace 'your_api_key_here' with your actual OpenWeather API key
nano .env  # or use your preferred editor
```

### 3. Install Dependencies with uv

```bash
# Sync dependencies (creates virtual environment and installs packages)
uv sync
```

This will:
- Create a virtual environment in `.venv/`
- Install `requests` library for HTTP API calls
- Install `python-dotenv` for environment variable management

## How to Run

Run the application using uv:

```bash
uv run python main.py
```

**Interactive Usage:**
1. The app will prompt you to enter a location
2. Type a city name (e.g., "London", "Tokyo", "New York")
3. Press Enter
4. View the air quality data for that location

## Example Usage

### Successful Query

```bash
$ uv run python main.py
Welcome to the Air Pollution App!
------------------------------------------------------------
Enter a location (city name): London

Fetching coordinates for 'London'...
Found: 51.5073°, -0.1276°
Fetching air quality data...

============================================================
Air Quality Data for London
Coordinates: 51.5073°, -0.1276°
============================================================

Air Quality Index (AQI): 2 - Fair

Pollutant Concentrations (μg/m³):
  CO (Carbon Monoxide):        144.28
  NO (Nitrogen Monoxide):      0.10
  NO₂ (Nitrogen Dioxide):      11.61
  O₃ (Ozone):                  70.68
  SO₂ (Sulfur Dioxide):        5.50
  PM2.5 (Fine Particles):      4.58
  PM10 (Coarse Particles):     5.42
============================================================
```

### AQI Quality Levels

The Air Quality Index (AQI) uses a 1-5 scale:
- **1 - Good** — Air quality is satisfactory
- **2 - Fair** — Acceptable air quality
- **3 - Moderate** — May cause issues for sensitive individuals
- **4 - Poor** — Health effects may be experienced
- **5 - Very Poor** — Serious health effects possible

## Error Handling

The application handles various error scenarios gracefully:

### Invalid Location
```bash
Enter a location (city name): XYZ12345

Fetching coordinates for 'XYZ12345'...
Error: Location 'XYZ12345' not found. Please try a different location.
```

### Missing API Key
```bash
Error: API_KEY not found in .env file.
Please create a .env file with your OpenWeather API key.
See .env.example for reference.
```

### Invalid API Key
```bash
Fetching coordinates for 'London'...
Error: Invalid API key. Please check your .env file.
```

### Network Issues
```bash
Fetching coordinates for 'London'...
Error: Could not connect to OpenWeather API. Please check your internet connection.
```

### Other Error Scenarios:
- **Empty location input** — Prompts user that location cannot be empty
- **Request timeout** — Warns about connection issues
- **Invalid coordinates** — Validates lat/lon ranges (-90 to 90, -180 to 180)
- **Malformed API responses** — Handles parsing errors gracefully

## Development

### Type Checking

All functions include PEP 484 type hints. To verify types:

```bash
# Install mypy for type checking
uv pip install mypy

# Run type checker
uv run mypy main.py api_client.py
```

### Code Structure

- **Separation of Concerns** — API logic separated from UI logic
- **Type Safety** — All functions have parameter and return type annotations
- **Error Handling** — Comprehensive try-catch blocks with user-friendly messages
- **Input Validation** — Validates all inputs before API calls

## Comparing Your Progress

If you're working on this as an educational project, you can compare your implementation with demo branches:

### Fork and Setup for Comparison

1. **Fork the Repository on GitHub**
   - Go to: https://github.com/curiosity-unlimited/air-pollution-app.git
   - Click the "Fork" button
   - **IMPORTANT:** Uncheck "Copy the DEFAULT branch only" to copy all branches
   - Your fork: https://github.com/YOUR-USERNAME/air-pollution-app

2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/air-pollution-app
   cd air-pollution-app
   ```

3. **Fetch all branches and tags:**
   ```bash
   git fetch origin --tags
   git branch -a
   ```

4. **Create your development branch:**
   ```bash
   git checkout -b develop/agent-mode
   # or
   git checkout -b develop/plan-agent-mode
   ```

5. **Compare with demo implementations:**
   ```bash
   # List all milestones
   git tag -n
   
   # Compare with a specific milestone
   git diff your-branch-name..tag-name
   
   # See all differences between your work and the reference
   git diff your-branch-name..demo/agent-mode
   git diff your-branch-name..demo/plan-agent-mode
   ```

For a comprehensive guide, see [`CONTRIBUTING.md`](./CONTRIBUTING.md)

## Contributing

Contributions are welcome! Please follow the guidelines in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## License

[MIT](LICENSE)