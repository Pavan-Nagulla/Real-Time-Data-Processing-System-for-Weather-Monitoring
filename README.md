# Weather Monitoring System

## DISCLAIMER

### We have rewritten the commit history due to a faulty commit. This serves as a reminder to double-check changes before making a PR. You have ample time to work on an issue once assigned, so avoid rushing PRs. If you're a recurring contributor, take a fresh fork. New contributors can start contributing right away!

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Environment Variables](#environment-variables)
- [Running Unit Tests](#running-unit-tests)
- [Future Enhancements](#future-enhancements)
- [GitHub Repository](#github-repository)
- [License](#license)

---

## Project Overview

The **Weather Monitoring System** is a Python-based application that retrieves weather data from multiple cities, processes it, stores it in an SQLite database, and visualizes key metrics such as temperature and humidity. The system also includes an alerting mechanism to send email notifications when certain weather conditions (e.g., high temperature) are met.

It uses the OpenWeatherMap API and supports data visualization through `matplotlib` and `seaborn` libraries.

---

## Features

- **Fetch Weather Data**: Retrieves real-time weather data (temperature, humidity) using OpenWeatherMap API.
- **Data Storage**: Stores weather data in an SQLite database for persistence.
- **Email Alerts**: Sends email notifications when predefined weather thresholds (e.g., temperature > 35°C) are exceeded.
- **Data Visualization**: Generates graphical representations of temperature and humidity trends over time.
- **Unit Testing**: Includes unit tests for key modules in the system.

---

## Technologies

- **Backend**: Python 3.13
- **Database**: SQLite
- **Visualization**: Matplotlib, Seaborn
- **API**: OpenWeatherMap API
- **Email**: smtplib
- **Testing**: Unittest

---

## Getting Started

### Prerequisites

- **Python 3.13** or later
- **pip** (Python package manager)


## Install the required Python packages:

## bash
 ``` Copy code
pip install -r requirements.txt
Set up environment variables in a .env file:
```

```
bash
Copy code
API_KEY=your_openweathermap_api_key
EMAIL_SENDER=your_email_address
EMAIL_PASSWORD=your_email_password
EMAIL_RECIPIENT=recipient_email_address
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
Run the application:
```
```
bash
Copy code
python src/main.py
To visualize weather data:
```
```
bash
Copy code
python src/visualizer.py
```