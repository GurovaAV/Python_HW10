import requests

city = input('Введите название города: ')

#Спасибо сайту @igor_chubin за такой чудо графический прогноз!
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

print(res.text)