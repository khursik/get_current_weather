import pprint
import requests

class OpenWeatherForecast:

    def get(self, city):
        url = f"https://samples.openweathermap.org/data/2.5/weather?q={city},uk&appid=439d4b804bc8187953eb36d2a8c26a02"
        data = requests.get(url).json()
        forecast_data1 = data["weather"]
        forecast_data2 = [data["main"]]
        forecast = []
        for data1 in forecast_data1:
            forecast.append({
                "description": data1["description"]
            })
        for data2 in forecast_data2:
            forecast.append({
                "temp": data2["temp"]
            })
        return forecast

class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)

def _main():
    city_info = CityInfo("Moscow")
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)        


if __name__=='__main__':
    _main()