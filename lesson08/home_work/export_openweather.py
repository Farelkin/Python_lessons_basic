
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""


import requests
import sqlite3
import os
a = open("app.id")
my_app_id = a.read().splitlines()
api_url = "http://api.openweathermap.org/data/2.5/weather"
city = input("Пожалуйста введите город на английском языке: ")
data_list = {"q": city, "appid": my_app_id, "units": "metric"}
a.close()
inquiry = requests.get(api_url, params=data_list)  # Отправим запрос на получение данных
data = inquiry.json()  # Сохраним полученные данные
conclusion = "Температура в городе {} сейчас {} градус(ов)"
print(conclusion.format(city, data["main"]["temp"])) # Вытаскиваем градусы из данных
save_data = input("Хотите сохранить данные в SQLite? y/n: ")

if save_data == "y" or "Y":
    weather = [(data["sys"]["id"], city, data["dt"], data["main"]["temp"],
                data["main"]["temp"])]  # Записываем необходимые данные
    connect = sqlite3.connect("{}.db".format(city))
    c = connect.cursor()
    if os.path.isfile("{}.db".format(city)):  # Если БД уже есть - обновляем
        c.execute("""REPLACE INTO weather (id_города, Город, Дата, Температура, 
        id_погоды) VALUES (?, ?, ?, ?, ?)""",
                  (data["sys"]["id"], city, data["dt"], data["main"]["temp"], data["main"]["temp"]))
        # Обновляем значения в БД
        connect.commit()  # UPDATE weather SET id_города=?, Город=?, Дата=?, Температура=?, id_погоды=? WHERE ?
        c.close()
        connect.close()
        print("Такая база уже существует. Мы её обновили!")
    else:  # Если БД ещё нет - создаём
        c.execute('''CREATE TABLE weather (id_города INTEGER PRIMARY KEY, 
        Город VARCHAR(255), Дата DATE, Температура INTEGER, id_погоды INTEGER)''')
        c.executemany("INSERT INTO weather VALUES (?, ?, ?, ?, ?)", weather)  # Добавляем значения в БД
        connect.commit()
        c.close()
        connect.close()
        print("База данных {}.db создана!".format(city))
else:
    print("Хорошо, создавать БД не будем. Приятного дня!")
