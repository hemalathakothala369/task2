import requests

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8365a877c89f5c31a8f06472f3c61324&units=metric"

try:
    response = requests.get(url)

    # Check API status
    if response.status_code == 200:

        data = response.json()

        # Extract data from JSON
        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print("\nWeather Details")
        print("-------------------")
        print("City:", city_name)
        print("Temperature:", temperature, "°C")
        print("Weather:", weather)
        print("Humidity:", humidity, "%")

    else:
        print("City not found or API error!")

except requests.exceptions.RequestException:
    print("Internet connection error!")