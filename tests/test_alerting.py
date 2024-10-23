# tests/test_alerting.py

import unittest
from src.alerting_system import check_alerts, alert_history  # Import alert_history to reset it

import unittest
from src.alerting_system import alert_history

class TestAlertingSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize alert history for tests
        cls.cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
        for city in cls.cities:
            alert_history[city] = {'temperature': [], 'humidity': [], 'alerts': []}

    # You can now add your test methods here
    def test_alert_conditions(self):
        # Example test method
        self.assertIn('Delhi', alert_history)
        self.assertIn('temperature', alert_history['Delhi'])
        self.assertIn('humidity', alert_history['Delhi'])
        self.assertIn('alerts', alert_history['Delhi'])

# More tests can be added as necessary

    def test_temperature_alert(self):
        city = 'Delhi'
        threshold = 35  # Example threshold
        condition = 'Clear'
        wind_speed = 5  # Add appropriate wind speed for your checks
        check_alerts(city, 32, condition, wind_speed)  # First below threshold
        check_alerts(city, 36, condition, wind_speed)  # Second above threshold

    def test_no_alert(self):
        city = 'Mumbai'
        threshold = 35
        condition = 'Clear'
        wind_speed = 3  # Ensure this is defined
        check_alerts(city, 30, condition, wind_speed)  # Below threshold

if __name__ == '__main__':
    unittest.main()
