import requests
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import asyncio
import aiohttp


load_dotenv()

API_KEY = os.getenv("API_KEY")


class Weather(BaseModel):
    city: str
    temperature: float
    condition: str



def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)
    data = response.json()

    weather = Weather(city=data["location"]["name"], temperature=data["current"]["temp_c"], condition=data["current"]["condition"]["text"] )

    return weather



async def get_weather_async(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            data = await response.json()

            weather = Weather(
                city=data["location"]["name"],
                temperature=data["current"]["temp_c"],
                condition=data["current"]["condition"]["text"]
            )

            return weather



def save_report(weather):
    with open("report.txt", "w") as file:
        file.write(f"City: {weather.city}\n")
        file.write(f"Temperature: {weather.temperature}°C\n")
        file.write(f"Condition: {weather.condition}\n")



if __name__ == "__main__":

    city = input("Enter city name: ")
    weather = get_weather(city)

    print("\nWeather Report")
    print(weather)

    save_report(weather)

    print("\nReport saved in report.txt")

  
    print("\nRunning async version...")

    async_weather = asyncio.run(get_weather_async(city))

    print(async_weather)