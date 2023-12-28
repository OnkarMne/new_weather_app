from weather_brain import Weather
from weather_ui import Weatherapp
import os

api_key = os.environ.get("API_KEY")

current = Weather(api_key)

wui = Weatherapp(current)

