from dotenv import load_dotenv
import os
import requests

load_dotenv()

weather_api = os.getenv("API_KEY")
url = os.getenv("BASE_URL")

city = input("Please enter a city name: ")
request_url = f"{url}?appid={weather_api}&q={city}"

# Send request to the URL
response = requests.get(request_url)
# Check if response is OK
if response.status_code == 200:
    data = response.json()
    current_weather = data["weather"][0]["description"]
    current_temp = round(data["main"]["temp"] - 273.15, 2)

    print("Current weather is: ", current_weather)
    print("The temperature is: ", current_temp, "celsius")
else:
    print("An Error Occurred.")
