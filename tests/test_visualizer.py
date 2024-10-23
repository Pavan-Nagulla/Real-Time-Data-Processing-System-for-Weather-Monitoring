# tests/test_visualizer.py

import unittest
from unittest.mock import patch
from src.visualizer import visualize_weather_data


class TestVisualizer(unittest.TestCase):

    @patch('matplotlib.pyplot.show')  # Mock plt.show() to prevent the plot from displaying
    def test_plot_daily_summary(self, mock_show):
        summary_data = {'avg_temp': 25, 'max_temp': 30, 'min_temp': 20}
        visualize_weather_data(summary_data)  # This should not raise an error

if __name__ == '__main__':
    unittest.main()
