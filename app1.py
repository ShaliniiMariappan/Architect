from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "a24a4a7b8c4e0d1e4be3e723606d43ba"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


@app.route('/weather', methods=['POST'])
def get_weather():
    city_name = request.form['city']
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_condition_code = data['weather'][0]['id']
        chance_of_rain = "Low"
        if weather_condition_code >= 500 and weather_condition_code < 600:
            chance_of_rain = "High"

        result = {
            "weather_data": (
                f"Weather in {city_name.capitalize()}:"
                f"Temperature: {round(temperature - 273.15, 2)} C"
                f"Description: {weather_description.capitalize()}"
                f"Humidity: {humidity}%"
                f"Wind Speed: {wind_speed} m/s"
                f"Chance of Rain: {chance_of_rain}"
            )
        }
        return jsonify(result)
    else:
        error_message = "Error fetching weather data. Please check your input or try again later."
        
if __name__ == "__main__":
    app.run(debug=True)