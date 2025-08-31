import requests
from datetime import datetime
import schedule
import time
from db import create_table, insert_weather
from logger_config import setup_logger

logger = setup_logger()

API_KEY = "KEY"   # Skriv in din api nyckel här
CITY = "Stockholm" #Skriv in din stad här
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    """
    Hämtar väderdata från OpenWeatherAPI.

    Returns:
        tuple: (temp, weather_description, timestamp_iso8601)

    Raises:
        Exception: Om API-anropet misslyckas eller datan inte innehåller väntade fält.
    """
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "main" not in data or "weather" not in data:
            raise ValueError(f"Oväntad API-respons: {data}")

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        timestamp = datetime.utcnow().isoformat()

        logger.info(f"Hämtade väder: {temp}°C, {weather}")
        return temp, weather, timestamp
    except Exception as e:
        logger.error(f"Fel vid API-anrop: {e}")
        raise

def job():
    """
    Kör ett fullständigt ETL-jobb:
    1. Skapar tabellen om den inte finns.
    2. Hämtar väderdata.
    3. Infogar datan i databasen.
    """
    try:
        create_table()
        temp, weather, timestamp = fetch_weather()
        insert_weather(temp, weather, timestamp)
        logger.info("Väderdata insatt i MSSQL-databasen.")
    except Exception as e:
        logger.error(f"Fel i ETL-jobbet: {e}")

def main():
    """
    Schemalägger jobbet att köras varje timme och håller processen igång.
    """
    schedule.every(1).hours.do(job)  # Här kan du välja att köra varje timme till exempel

    logger.info("Schemaläggning startad. Kör ETL-jobb varje timme.")
    job()  # Här kan du välja att köra direkt första gången

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

