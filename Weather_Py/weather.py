import tkinter as tk
from tkinter import messagebox
import requests
from environs import Env
import os
env = Env()
env.read_env(".env")
api_key = os.getenv("api_key")


def get_weather_data(city, units='metric'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}'
    response = requests.get(url)
    return response.json()


def parse_weather_data(data):
    if data.get('cod') != 200:
        return None

    return{
        'location': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['weather'][0]['description'],
        'wind-speed': data['wind']['speed'],
    }

def fetch_weather():
    city = city_entry.get()
    units = units_var.get()

    if not city:
        messagebox.showerror("Input Error","Please enter a city name.")
        return
    

    weather_data = get_weather_data(city, units)
    weather = parse_weather_data(weather_data)

    if weather: 
        weather_info = (
        f"Location: {weather['location']}\n"
        f"Tempeature: {weather['temperature']}°\n"
        f"Humidity: {weather['humidity']}%\n"
        f"Wind-Speed: {weather['wind-speed']} m/s"
        )
        weather_label.config(text=weather_info)

    else:
        weather_label.config(text="Could not retrieve weather data.")

root = tk.Tk()
root.title("Weather App")

#City input
tk.Label(root, text="Enter City:").grid(row=0, column=0)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1)

#Unit selection
units_var = tk.StringVar(value="metric") #Default to Celsius
tk.Label(root, text="Select Units:").grid(row=1, column=0)
tk.Radiobutton(root, text="Celsius", variable=units_var, value="metric").grid(row=1, column=1)
tk.Radiobutton(root, text="Fahrenheit", variable=units_var, value="imperial").grid(row=1, column=2)

#Button to fetch weather
fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.grid(row=2, column=1)

#Label to display weather
weather_label = tk.Label(root, text="")
weather_label.grid(row=3, column=0, columnspan=2)

root.mainloop()