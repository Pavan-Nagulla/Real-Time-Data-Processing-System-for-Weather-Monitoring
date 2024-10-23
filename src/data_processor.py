import sqlite3
from collections import Counter
from config.config import TEMP_UNIT

# Helper functions for temperature conversion
def convert_kelvin_to_celsius(temp_kelvin):
    """Convert temperature from Kelvin to Celsius."""
    return temp_kelvin - 273.15

def convert_kelvin_to_fahrenheit(temp_kelvin):
    """Convert temperature from Kelvin to Fahrenheit."""
    return (temp_kelvin - 273.15) * 9/5 + 32

class WeatherDataProcessor:
    def __init__(self):
        # Dictionary to store daily weather data for each city
        self.daily_data = {}

    def process_data(self, city, weather_data):
        """Process the raw weather data and update the tracked data for rollups."""
        try:
            # Extract temperature, weather condition, humidity, and wind speed
            main_weather = weather_data['weather'][0]['main']
            temp_kelvin = weather_data['main']['temp']
            feels_like_kelvin = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            
            # Convert temperature based on user preference (Celsius/Fahrenheit)
            if TEMP_UNIT == "Celsius":
                temperature = convert_kelvin_to_celsius(temp_kelvin)
                feels_like = convert_kelvin_to_celsius(feels_like_kelvin)
            else:
                temperature = convert_kelvin_to_fahrenheit(temp_kelvin)
                feels_like = convert_kelvin_to_fahrenheit(feels_like_kelvin)

            # Track the data for the city
            if city not in self.daily_data:
                self.daily_data[city] = {'temps': [], 'conditions': [], 'humidity': [], 'wind_speed': []}

            self.daily_data[city]['temps'].append(temperature)
            self.daily_data[city]['conditions'].append(main_weather)
            self.daily_data[city]['humidity'].append(humidity)
            self.daily_data[city]['wind_speed'].append(wind_speed)

        except KeyError as e:
            print(f"Missing key in weather data: {e}")
            return None  # Handle missing key gracefully

    def calculate_daily_summary(self, city):
        """Calculate and return the daily weather summary for the city."""
        if city not in self.daily_data:
            return None  # No data available for this city

        temps = self.daily_data[city]['temps']
        conditions = self.daily_data[city]['conditions']
        humidity = self.daily_data[city]['humidity']
        wind_speed = self.daily_data[city]['wind_speed']
        
        # Calculate average, max, min temperatures and dominant condition
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        avg_humidity = sum(humidity) / len(humidity)
        avg_wind_speed = sum(wind_speed) / len(wind_speed)
        dominant_condition = Counter(conditions).most_common(1)[0][0]  # Most frequent condition

        return {
            'city': city,
            'average_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'average_humidity': avg_humidity,
            'average_wind_speed': avg_wind_speed,
            'dominant_condition': dominant_condition
        }

    def store_daily_summary(self, summary):
        """Store the daily summary in a SQLite database."""
        if summary is None:
            print("No summary to store.")
            return

        conn = sqlite3.connect('data/daily_summaries.db')
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_summary (
                city TEXT,
                average_temp REAL,
                max_temp REAL,
                min_temp REAL,
                average_humidity REAL,
                average_wind_speed REAL,
                dominant_condition TEXT
            )
        ''')

        # Insert daily summary into the database
        cursor.execute('''
            INSERT INTO weather_summary (city, average_temp, max_temp, min_temp, average_humidity, average_wind_speed, dominant_condition)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (summary['city'], summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['average_humidity'], summary['average_wind_speed'], summary['dominant_condition']))
        
        conn.commit()
        conn.close()

    def reset_daily_data(self):
        """Clear daily data after storing the summary (to start fresh for the next day)."""
        self.daily_data = {}
