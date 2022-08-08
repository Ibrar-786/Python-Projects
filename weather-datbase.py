import requests
import datetime as dt
import mysql.connector
import time

mydb = mysql.connector.connect(
    host = 'localhost',
    user = '???',
    password = '???',
    database = 'weather'
)

mycursor = mydb.cursor()

city = ('Watford')

api_key = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=f2b5f83c3c32235c9aab785f61560fec'

def weather_retrival():

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

    sql = "INSERT INTO Weather (conditions, temp, feelsLike, maxTemp, minTemp, pressure, humidity, windSpeed, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (condition, temperature, feels_like_temprature, max_temperature, min_temperature, pressure, humidity, wind_speed, time)

    mycursor.execute(sql, values)

    mydb.commit()

    print('Record Inserted')

if __name__ == '__main__':
    time.sleep(10)
    while True:
        weather_retrival()
        time.sleep(3600)

