import requests


server_url = "http://localhost:5003/get_weather"


def main():
        city_name = input("Погода для города: ")

        params = {"city": city_name}

        weather_response = requests.get(server_url, params=params)

        if weather_response.status_code == 200:
                weather_data = weather_response.json()

                output = "Температура: {temp}°C, {desc}, скорость ветра: {wind} м/c, влажность: {humi}%, давление: {pres} гПа".format(
                        temp=weather_data["temperature"],
                        desc=weather_data["weather"],
                        wind=weather_data["wind"],
                        humi=weather_data["humidity"],
                        pres=weather_data["pressure"]
                )
        elif weather_response.status_code == 404:
                output = "Ошибка: отсутствует название города"
        elif weather_response.status_code == 405:
                output = "Ошибка: неверное название города"
        else:
                output = "Ошибка: нет ответа от сервиса"

        print(output)




if __name__ == "__main__":
        main()
