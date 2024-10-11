import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(city, units="imperial"):
    api_key = ""
    url = ""
    response = requests.get(url)
    return response.json()

def parse_data(data):
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
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    

    weather_data = get_weather_data(city, units)
    weather = parse_data(weather_data)

    if weather:
        weather_info = (
            f"Location: {weather['location']}\n "
            f"Temperature: {weather['temperature']}°\n"
            f"Description: {weather['description']}\n"
            f"Wind-Speed: {weather['wind-speed']} m/s"
        )
        weather_label.config(text=weather_info)
    else:
        weather_label.config(text="")
    
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter a city name: ")
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=0)

units_var = tk.StringVar(value="imperial")
tk.Label(root, text="Select Units:").grid(row="",column="")
tk.Radiobutton(root, text="Celsius", variable=units_var, value="metric").grid(row="", column="")
tk.Radiobutton(root, text="Fahrenheit", variable=units_var, value="imperial").grid(row="", column="")


fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.grid(row="", column="")

weather_label = tk.Label(root, text="")
weather_label.grid(row="", column="")

root.mainloop()