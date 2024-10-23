Weather Monitoring System
Project Overview
The Weather Monitoring System is a Python-based application that retrieves weather data for multiple cities, processes this data, stores it in a local SQLite database, and visualizes key metrics such as temperature and humidity trends. The system also features an alerting mechanism that sends email notifications when certain weather conditions (like high temperatures or humidity) are met.

This project uses data from the OpenWeatherMap API and supports visualization through matplotlib and seaborn libraries. The system can be extended to handle more cities and additional weather parameters.

Features
Fetch Weather Data: Retrieves weather data (temperature, humidity) for multiple cities using the OpenWeatherMap API.
Process and Store Data: Saves the fetched weather data into an SQLite database for persistence.
Alerts: Sends email alerts when certain weather thresholds (e.g., temperature > 35°C) are exceeded.
Visualizations: Displays graphical representations of the collected data, such as temperature and humidity trends over time.
Unit Testing: Includes unit tests to verify the functionality of various components in the system.
Table of Contents
Installation
Usage
Features
Technologies Used
Environment Variables
Running Unit Tests
Future Enhancements
GitHub Repository
Installation
Prerequisites:
Before you begin, ensure you have the following installed:

Python 3.13 or later
pip (Python package installer)
Steps to Install:
Clone the GitHub Repository: Clone the repository from GitHub to your local machine.

bash
Copy code
git clone https://github.com/your-username/weather-monitoring-system.git
cd weather-monitoring-system
Create a Virtual Environment (optional but recommended): It is advisable to create a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\activate   # On Windows
Install Required Packages: Use the requirements.txt file to install all necessary Python packages:

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables: Create a .env file in the root of the project directory and add the following environment variables:

bash
Copy code
API_KEY=your_openweathermap_api_key
EMAIL_SENDER=your_email_address
EMAIL_PASSWORD=your_email_password
EMAIL_RECIPIENT=recipient_email_address
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
These are required for:

Accessing the OpenWeatherMap API
Sending email alerts when weather thresholds are met
Verify Database Initialization: Make sure that an SQLite database file weather.db is present in the data/ directory. The program will auto-create the necessary table (weather_summary) if it does not exist.

Usage
Fetching Weather Data:
To retrieve weather data for the predefined list of cities and store it in the SQLite database, run the following command:

bash
Copy code
cd src
python main.py
This will fetch the current weather data for cities like Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad, and store them in the database.

Visualizing Data:
You can visualize the collected weather data by running the following command:

bash
Copy code
python visualizer.py
This will display graphs showing temperature and humidity trends over the last few days.

Sending Alerts:
The system will automatically send an email alert if the weather data exceeds predefined thresholds (e.g., temperature > 35°C). If you want to check or trigger alerts manually, you can modify the alerting_system.py file and its thresholds.

Technologies Used
This project leverages several technologies to accomplish its functionality:

Python 3.13: Main programming language used for development.
OpenWeatherMap API: To fetch real-time weather data for different cities.
SQLite: To store weather data locally in a lightweight database.
Pandas: For data manipulation and analysis.
Matplotlib & Seaborn: For data visualization (graph plotting).
smtplib: For sending email alerts when weather conditions meet thresholds.
Unittest: For unit testing the different components of the system.
Environment Variables
Ensure that you set the following environment variables in the .env file:

API_KEY: Your OpenWeatherMap API key to fetch the weather data.
EMAIL_SENDER: The email address from which the alert emails will be sent.
EMAIL_PASSWORD: The password for the email account used to send alerts.
EMAIL_RECIPIENT: The recipient email address for receiving alerts.
SMTP_SERVER: The SMTP server for your email provider (e.g., smtp.gmail.com for Gmail).
SMTP_PORT: The port number for your email provider’s SMTP server (typically 587 for TLS).
Running Unit Tests
The project includes unit tests for each module in the tests/ directory. To run all tests, use the following command:

bash
Copy code
python -m unittest discover tests
If all tests pass, you should see output similar to:

Copy code
Ran 7 tests in 0.200s

OK
Future Enhancements
City Customization: Add functionality to allow users to input cities of their choice for weather monitoring.
Extended Weather Metrics: Track and alert on additional weather metrics such as wind speed, air pressure, etc.
Web Interface: Build a simple web interface for users to interact with the system and visualize data in real time.
Weather Data Aggregation: Add functionality to store historical weather data and visualize trends over longer periods.


Flowdata : 
weather_monitoring_system/
│
├── config/
│   └── config.py             # Configuration file for API keys, locations, and thresholds
    └── __init__.py
│
├── data/
│   └── daily_summaries.db     # SQLite or other database to store daily summaries
│
├── src/
│   ├── data_retriever.py      # Retrieves data from the OpenWeatherMap API
│   ├── data_processor.py      # Processes and calculates rollups and aggregates
│   ├── alerting_system.py     # Checks and triggers alerts based on thresholds
│   ├── visualizer.py          # For generating visualizations
│   └── main.py                # Entry point of the system to run the monitoring
│
├── tests/
│   ├── test_data_retriever.py  # Tests for API data retrieval and parsing
│   ├── test_processor.py       # Tests for temperature conversion and rollup calculations
│   ├── test_alerting.py        # Tests for alert triggering based on thresholds
│   └── test_visualizer.py      # Tests for visualizations
    └── __init__.py 
│
├── requirements.txt           # Required Python libraries
└── README.md                  # Project documentation
