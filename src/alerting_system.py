import smtplib
from email.mime.text import MIMEText
from config.config import (
    ALERT_THRESHOLD_TEMP,
    ALERT_THRESHOLD_HUMIDITY,
    ALERT_THRESHOLD_WIND_SPEED,
    ALERT_CONSECUTIVE_UPDATES,
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECIPIENT,
    SMTP_SERVER,
    SMTP_PORT,
)

# Initialize alert_history for specified cities
alert_history = {
    city: {'temperature': [], 'humidity': [], 'alerts': []} for city in 
    ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
}

def send_email_alert(city, alert_type, current_value):
    """Send an email alert for a specific city when conditions exceed thresholds."""
    subject = f"Weather Alert: {alert_type} in {city} exceeded threshold!"
    body = f"Alert: {alert_type} in {city} is now {current_value}, which exceeds the threshold."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, msg.as_string())
        print(f"Email alert sent for {city}: {alert_type} exceeded threshold.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def check_alerts(city, temp, condition, wind_speed):
    """Check the alert conditions based on the weather data."""
    # Ensure city exists in alert_history
    if city not in alert_history:
        print(f"City {city} not found in alert history.")
        return

    # Get the last humidity value or default to 0 if not available
    humidity = alert_history[city]['humidity'][-1] if alert_history[city]['humidity'] else 0

    try:
        humidity = float(humidity)
    except ValueError:
        print(f"Invalid humidity value for {city}: {humidity}")
        return

    # Trigger alerts based on temperature and humidity thresholds
    if temp > ALERT_THRESHOLD_TEMP or humidity >= ALERT_THRESHOLD_HUMIDITY:
        alert_history[city]['alerts'].append("Alert condition met")
        print(f"Alert for {city}: Temperature = {temp}, Humidity = {humidity}")

        # Send email alert for temperature
        if temp > ALERT_THRESHOLD_TEMP:
            send_email_alert(city, "Temperature", temp)

        # Send email alert for humidity
        if humidity >= ALERT_THRESHOLD_HUMIDITY:
            send_email_alert(city, "Humidity", humidity)

    # Update alert history with the latest readings
    alert_history[city]['temperature'].append(temp)
    alert_history[city]['humidity'].append(humidity)

