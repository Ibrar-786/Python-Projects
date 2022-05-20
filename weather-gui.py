import json
import tkinter as tk
import requests
import datetime as dt

def getWeather(canvas):

    city = texfield.get()
    api_key = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=f2b5f83c3c32235c9aab785f61560fec'

    # Gets data from the api and loads them into these variables
    json_data = requests.get(api_key).json()
    condition = json_data['weather'][0]['main']
    #description = json_data['weather'][0]['description']
    temperature = int(json_data['main']['temp'] - 273.15)
    min_temperature = int(json_data['main']['temp_min'] - 273.15)
    max_temperature = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise = dt.datetime.utcfromtimestamp(json_data['sys']['sunrise'] + json_data['timezone'])
    sunset = dt.datetime.utcfromtimestamp(json_data['sys']['sunset'] + json_data['timezone'])


    # Prints out the results on the screen
    final_info = condition + '\n' + str(temperature) + '°C' #+ '\n' + str(description)
    final_data = '\n' + 'Minimum Temprature: ' + str(min_temperature) + '\n' + 'Maximum Temprature: ' + str(max_temperature) + '\n' + 'Pressure: ' + str(pressure)  + '\n' + 'Humidity: ' + str(humidity) + '\n' + 'Wind Speed: ' + str(wind_speed) + '\n' + 'Sunrise: ' + str(sunrise)  + '\n' 'Sunset: ' + str(sunset)  

    label1.config(text = final_info)
    label2.config(text = final_data)

# Draws the screen
canvas = tk.Tk()
canvas.geometry('750x800')
canvas.title('Weather Application')

# Sets the font styling
f = ('helvetica', 30, 'bold')
t = ('helvetica', 40, 'bold')

texfield = tk.Entry(canvas, justify='center', width = 20, font = t)
texfield.pack(pady = 20)
texfield.focus()
texfield.bind ('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()