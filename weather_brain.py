import requests


class Weather:

    def __init__(self, apikey):
        self.api_key = apikey

    def get_weather(self, city):

        try:
            parameters = {
                "q": f"{city}",
                "appid": self.api_key,
            }

            response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
            response.raise_for_status()

            weather_data = response.json()
            description = weather_data["weather"][0]['description']
            condition = weather_data['weather'][0]['main']
            temperature = int(weather_data["main"]['temp'])-273
            pressure = weather_data["main"]['pressure']
            humidity = weather_data["main"]['humidity']
            wind = weather_data['wind']['speed']
            id = weather_data["weather"][0]['id']

            result = [condition, temperature, pressure, humidity, wind, description, id]

            return result
            # print(f"Current weather of {city} is : \n "
            #       f"Temperature : {temperature}\n "
            #       f"Pressure: {pressure}\n "
            #       f"Humidity: {humidity} \n "
            #       f"Description :{description} ")

        except Exception as e:
            return False


