# Weather Scraper

A simple Python script that scrapes weather forecast data for Kochi, India from timeanddate.com and saves it to a CSV file.

## Features

- Scrapes 7-day weather forecast including:
  - Day and date
  - Weather conditions
  - Temperature (high/low)
  - Wind speed
  - Precipitation chance

## Requirements

- Python 3.8+
- Required packages:
  - requests
  - beautifulsoup4
  - pandas

## Setup

1. Clone this repository:
```bash
git clone https://github.com/Vishnudrm/weather_scrap.git
cd weather_scrap
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv myenv
myenv\Scripts\activate  # On Windows
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Simply run the scraper script:
```bash
python scraper.py
```

The script will create a `weather_forecast.csv` file containing the weather forecast data.

## Output Format

The CSV file contains the following columns:
- Day: Day of the week and date (e.g., "Mon11 Aug")
- Weather: Weather conditions description
- Temp: Temperature range in Celsius
- Wind: Wind speed in km/h
- Precip: Precipitation information

## License

This project is open source and available under the MIT License.
