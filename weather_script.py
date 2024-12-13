import requests

API_KEY = 'e49ac13d681c1b14b96885d37f90e0a8'  # Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_json_response(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    return get_json_response(BASE_URL, params)

def main():
    city_name = input("Enter city name: ")
    try:
        weather_data = get_weather(city_name)
        print(f"Weather in {city_name}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    except Exception as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    main()