#  api_key = "6ec2ea8c4aeb7d849fc4e1623f7394f0"
import requests
import argparse

def get_location_weather(location: str, api_key: str):
    """
    Get the weather information for a specific location from the OpenWeatherMap API.

    Args:
        location (str): The name of the location.
        api_key (str): The API key for accessing the OpenWeatherMap API.

    Returns:
        dict: Weather information for the specified location in JSON format.
    """
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(location, api_key)
    res = requests.get(url)
    data = res.json()
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get weather information for a specific location.")

    parser.add_argument("--location", type=str, help="Name of the location")
    parser.add_argument("--api_key", type=str, help="API key for OpenWeatherMap API")

    args = parser.parse_args()

    weather_data = get_location_weather(args.location, args.api_key)

    print(weather_data)
