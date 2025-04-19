from flask import Flask, jsonify, request
import requests


app = Flask(__name__)

base_url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "e322f8c0fefe1bb37d4b7a5f7db2aabc"


@app.route('/get_weather', methods=['GET'])
def get_weather():
        city_name = request.args.get('city')

        if not city_name:
                return jsonify({"error": "Не указано название города"}), 404

        params = {
                "q": city_name,
                "appid": api_key,
                "units": "metric",
                "lang": "ru"
        }

        weather_response = requests.get(base_url, params=params)

        if weather_response.status_code == 200:
                weather_data = weather_response.json()

                weather_json = {
                 "city": weather_data["name"],
                 "temperature": weather_data["main"]["temp"],
                 "feels_like": weather_data["main"]["feels_like"],
                 "weather": weather_data["weather"][0]["description"],
                 "wind": weather_data["wind"]["speed"],
                 "humidity": weather_data["main"]["humidity"],
                 "pressure": weather_data["main"]["pressure"]
                }

                return weather_json, 200
        else:
                return jsonify({"error": "Неверное название города"}), 405


if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5003)
