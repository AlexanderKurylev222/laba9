import requests
import tkinter as tk

def fetch_weather():
    api_key = "76bc2a4c6db194b9e6c5374f1cfbe7ba"
    city = "Ulyanovsk"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    try:
        response = requests.get(url, timeout=10) 
        print(f"Статус ответа: {response.status_code}")
        print(f"Ответ: {response.text}")
        response.raise_for_status()

        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        result = f"Погода в {city}:\n{weather.capitalize()}, температура: {temp}°C"
        
        result_label.config(text=result)
    except requests.exceptions.RequestException as e:

        result_label.config(text=f"Ошибка: Не удалось получить данные.\n{e}")
        print(f"Ошибка: {e}")

window = tk.Tk()
window.title("Прогноз погоды")

instruction_label = tk.Label(window, text="Нажмите на кнопку, чтобы узнать погоду в Ульяновске")
instruction_label.pack(pady=10)

button = tk.Button(window, text="Узнать погоду", command=fetch_weather)
button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

window.mainloop()
