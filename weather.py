import requests
import datetime as dt

print('This program will provide the weather details for any city')
city = input('Enter a city name : ')

api_key = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=f2b5f83c3c32235c9aab785f61560fec'

def main():

    # Gets the data stored in a JSON file using the openweather API and stores them in these variables.

    data = requests.get(api_key).json()
    condition = data['weather'][0]['main']
    temperature = int(data['main']['temp'] - 273.15)
    feels_like_temprature = int(data['main']['feels_like'] - 273.15)
    max_temperature = int(data['main']['temp_max'] - 273.15)
    min_temperature = int(data['main']['temp_min'] - 273.15)    
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    sunrise = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    time = dt.datetime.utcfromtimestamp(data['dt'])

    # Prints out the data to the screen

    print('--------------------------------------')
    print('          |', city,'|')
    print('--------------------------------------')
    print('Condition:', condition)
    print('Temperature:', temperature, '°C')
    print('Feels like:', feels_like_temprature, '°C')
    print('Maximum temperature:', max_temperature, '°C')
    print('Minimum temperature:', min_temperature, '°C')
    print('Pressure:', pressure, 'hPa') 
    print('Humidity:', humidity, '%')
    print('Windspeed:', wind_speed, 'm/s')
    print('Sunrise:', sunrise, 'local time')
    print('Sunset:', sunset, 'local time')
    print('Time:', time, 'local time')
    print('--------------------------------------')

main()