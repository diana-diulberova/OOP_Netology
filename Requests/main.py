import requests

# Загрузить файл на яндекс диск
# 1. Скачать файл на компьютер
response = requests.get('https://proza.ru/pics/2018/01/04/286.jpg')

if 200 <= response.status_code < 300:
    with open('robot.jpg', 'wb') as file:  # wb - потому что картинка jpg - это байты, а не текст
        file.write(response.content)

# 2. 
