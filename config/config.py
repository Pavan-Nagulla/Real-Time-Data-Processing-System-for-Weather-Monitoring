# config/config.py

# OpenWeatherMap API Configuration
API_KEY = "837dde66773d6b6c9fbf1433048b6d9b"   # Replace with your OpenWeatherMap API key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 60  # 60 seconds for quicker testing (1 minute)

# Thresholds
ALERT_THRESHOLD_TEMP = 30  # Example temperature threshold

ALERT_THRESHOLD_HUMIDITY = 70  # Example humidity threshold
ALERT_THRESHOLD_WIND_SPEED = 20  # Example: Wind speed threshold in m/s
ALERT_CONSECUTIVE_UPDATES = 3  # Trigger alert after this many consecutive high readings

# Temperature Unit
TEMP_UNIT = "Celsius"  # Options: "Celsius" or "Fahrenheit"

# Email Configuration
EMAIL_SENDER = "skyvartprogrammming@gmail.com"  # Your email address
EMAIL_PASSWORD = "jmqb esog aosv vtwx"  # Your email password
EMAIL_RECIPIENT = "skyvartprogrammming@example.com"  # Recipient's email address
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # For TLS
