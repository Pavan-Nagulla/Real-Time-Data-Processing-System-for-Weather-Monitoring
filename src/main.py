import sys
import os
import time
import schedule  # type: ignore

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_retriever import start_data_retrieval
from data_processor import WeatherDataProcessor
from data_storage import init_db, store_daily_summary
from config.config import INTERVAL
from visualizer import visualize_weather_data

# Initialize the weather data processor
processor = WeatherDataProcessor()

import threading

def run_weather_monitoring_system():
    """Main function to fetch and process weather data."""
    # Start data retrieval
    start_data_retrieval(processor, interval=INTERVAL)  # Start continuous data retrieval with the processor
    
    # Call the visualization function immediately after fetching data
    visualize_weather_data()  # This will visualize the data fetched into the database


def store_daily_summaries():
    """Calculate and store daily summaries for each city at the end of the day."""
    print("Storing daily summaries...")
    for city in processor.daily_data.keys():
        summary = processor.calculate_daily_summary(city)
        if summary:
            processor.store_daily_summary(summary)
        else:
            print(f"No summary available for {city}")
    
    # Reset the data for the next day
    processor.reset_daily_data()

# Schedule the daily summary storage at the end of the day (23:59)
schedule.every().day.at("23:59").do(store_daily_summaries)

if __name__ == "__main__":
    # Initialize the database before starting the monitoring system
    init_db()

    # Start the weather monitoring system and visualize the data immediately
    run_weather_monitoring_system()  # This will fetch, process, and visualize weather data
    schedule.run_pending()  # Check if it's time to store daily summaries
    time.sleep(1)  # Prevent tight looping
