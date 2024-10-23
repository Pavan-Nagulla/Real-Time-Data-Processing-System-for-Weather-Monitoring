import unittest  # Ensure unittest is imported
from src.data_processor import WeatherDataProcessor  # Import the WeatherDataProcessor class

class TestWeatherProcessing(unittest.TestCase):
    
    def setUp(self):
        self.processor = WeatherDataProcessor()  # Create an instance of WeatherDataProcessor

    def test_process_weather_data(self):
        weather_data = {
            'weather': [{'main': 'Clear'}],
            'main': {'temp': 293.15, 'feels_like': 295.15, 'humidity': 50},
            'wind': {'speed': 10}
        }

        self.processor.process_data('Delhi', weather_data)  # Process the data

        # Retrieve the processed data
        summary = self.processor.calculate_daily_summary('Delhi')

        # Ensure processed data contains expected keys
        self.assertIsNotNone(summary)
        self.assertIn('average_temp', summary)
        self.assertIn('max_temp', summary)
        self.assertIn('min_temp', summary)

        # Check if temperature is processed correctly
        # Adjust expected values based on your conversion logic
        self.assertAlmostEqual(summary['average_temp'], 20.0, places=1)  
        self.assertAlmostEqual(summary['max_temp'], 20.0, places=1)  
        self.assertAlmostEqual(summary['min_temp'], 20.0, places=1)  

    def test_missing_data(self):
        # Test for missing keys
        weather_data = {'main': {}}  # No weather condition
        result = self.processor.process_data('Delhi', weather_data)
        self.assertIsNone(result)  # Should return None on error

if __name__ == '__main__':
    unittest.main()  # Run the tests when this script is executed
