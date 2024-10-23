import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

def fetch_daily_summaries():
    """Fetch daily summaries from the SQLite database."""
    conn = sqlite3.connect('data/daily_summaries.db')
    query = "SELECT * FROM weather_summary"
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(df)  # For debugging, can be removed later
    return df

def visualize_weather_data(summary_data):
    """Visualize the weather data using Seaborn and Matplotlib."""
    
    if summary_data.empty:
        raise ValueError("DataFrame is empty, no data to visualize.")
    
    # Set the plot style
    sns.set(style="whitegrid")

    # Create a figure for plotting
    plt.figure(figsize=(14, 7))

    # Plot Temperature
    plt.subplot(2, 1, 1)  # Two rows, one column, first subplot
    sns.lineplot(data=summary_data, x='date', y='temperature', marker='o')
    plt.title('Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)

    # Plot Humidity
    plt.subplot(2, 1, 2)  # Two rows, one column, second subplot
    sns.lineplot(data=summary_data, x='date', y='humidity', marker='o', color='orange')
    plt.title('Humidity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

# Fetch data and visualize
summary_data = fetch_daily_summaries()
visualize_weather_data(summary_data)
