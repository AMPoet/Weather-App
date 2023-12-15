# Weather App

This is a simple weather application developed in Python using Tkinter for the GUI. The app allows users to search for a city and displays its current weather details along with local time.

## Features

- **Search Bar**: Enter the name of a city to retrieve its weather information.
- **Current Weather**: Displays temperature, weather condition, humidity, wind speed, pressure, and description.
- **Local Time**: Shows the local time of the searched city.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python (3.x recommended)
- Required Python libraries (`geopy`, `pytz`, `requests`, `timezonefinder`)

## How to Use

1. Clone the repository to your local machine.
2. Install the necessary libraries by running:
    ```
    pip install geopy pytz requests timezonefinder
    ```
3. Run the `weather_app.py` file using Python.
4. Enter the name of the city in the search bar and click the search icon.

## Acknowledgments

API: "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={apikey}

Libraries: 
  timezonefinder
  requests
  pytz
  geopy
