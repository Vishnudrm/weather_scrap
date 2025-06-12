import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_weather_forecast():
    url = "https://www.timeanddate.com/weather/india/kochi/ext"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="zebra tb-wt fw va-m tb-hover")
    rows = table.find_all("tr")

    forecast = []
    for row in rows[1:]:  # Skip header
        cols = row.find_all("td")
        if len(cols) >= 5:
            day = row.find("th").text.strip()
            weather = cols[1].text.strip()
            temp = cols[2].text.strip()
            wind = cols[3].text.strip()
            precip = cols[4].text.strip()
            forecast.append({
                "Day": day,
                "Weather": weather,
                "Temp": temp,
                "Wind": wind,
                "Precip": precip
            })

    if not forecast:
        print("⚠️ No weather data found.")
        return

    df = pd.DataFrame(forecast)
    df.to_csv("weather_forecast.csv", index=False)
    print("✅ 7-day weather forecast saved to weather_forecast.csv")

if __name__ == "__main__":
    scrape_weather_forecast()
