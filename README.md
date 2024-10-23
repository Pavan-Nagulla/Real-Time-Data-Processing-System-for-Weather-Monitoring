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
