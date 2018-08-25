import requests

a = open("app.id")
my_app_id = a.read().splitlines()
api_url = "http://api.openweathermap.org/data/2.5/weather"
city = "Moscow"
# city = input("Пожалуйста введите город на английском языке: ")
data_list = {"q": city, "appid": my_app_id, "units": "metric"}
a.close()
inquiry = requests.get(api_url, params=data_list)  # Отправим запрос на получение данных
data = inquiry.json()  # Сохраним полученные данные
conclusion = "Температура в городе {} сейчас {} градус(ов)"
print(data)
# print(conclusion.format(city, data["main"]["temp"]))  # Вытаскиваем градусы из данных
