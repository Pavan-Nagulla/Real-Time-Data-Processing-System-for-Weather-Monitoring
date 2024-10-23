import requests
import time
from config.config import API_KEY, CITIES, INTERVAL

def get_weather_data(city):
    """Fetch weather data for a specific city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"  # Using metric for Celsius
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error retrieving data for {city}: {response.status_code} - {response.text}")
        return None

def fetch_weather_for_all_cities():
    """Fetch weather data for all configured cities."""
    weather_data = []
    
    for city in CITIES:
        data = get_weather_data(city)
        if data:
            print(f"Successfully fetched weather data for {city}: {data}")  # Optional: Logging the data
            weather_data.append(data)
    
    return weather_data

def start_data_retrieval(processor, interval=INTERVAL):
    """
    Continuously fetch weather data for all cities at a given interval and process it.
    
    Args:
        processor: Instance of the data processor to process fetched weather data.
        interval: Time (in seconds) between consecutive API calls.
    """
    while True:
        print("Fetching weather data for all cities...")
        weather_data = fetch_weather_for_all_cities()
        
        for data in weather_data:
            city = data['name']  # Assuming the city name is in the 'name' key of the response
            processor.process_data(city, data)  # Process the data
        
        print(f"Waiting for {interval} seconds before the next data retrieval...")
        time.sleep(interval)  # Sleep for the interval duration before fetching again
