# tests/test_data_retriever.py

import unittest
from unittest.mock import patch
from src.data_retriever import fetch_weather_for_all_cities

class TestDataRetriever(unittest.TestCase):

    @patch('src.data_retriever.requests.get')
    def test_fetch_weather(self, mock_get):
        # Mock the API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {'temp': 293.15, 'feels_like': 295.15},
            'weather': [{'main': 'Clear'}]
        }
        
        # Call the function
        data = fetch_weather_for_all_cities()

        # Check that data returned is correct
        self.assertIsInstance(data, list)  # Should be a list
        # Check that we received weather data
        self.assertGreater(len(data), 0)  # Ensure some data is returned

if __name__ == '__main__':
    unittest.main()
