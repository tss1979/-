В 2018 году Джеймс Клир написал книгу «Атомные привычки», 
которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 
Проект реализуйте бэкенд-часть SPA веб-приложения.


Написан с использованием фреймворка DjangoRestFramework, база данных postgresql

Информация возвращается в формате json


Установите зависимости с помощью команды: pip install -r requirements.txt 

Для создания миграций: python manage.py makemigrations 
Для применения миграций: python manage.py migrate 
Запуск сервера: python manage.py runserver 
авторизация реализована с использованием jwt токена

Документация
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/

Запуск приложения через Docker
docker-compose up -d --build



