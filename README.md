# CI и CD проекта api_yamdb
***
![workflow](https://github.com/AleksanderMoosieno/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
### __Описание__x
***
#### Технологии:!
1. [Django](https://www.djangoproject.com)
2. [Django Rest Framework](https://www.django-rest-frvamework.org)
3. SQlite
4. JWT авторизацияc

__API__ стремится к __RESTFUL_ и представляет собой пffроект, который собир;;;ает отзывы
на произведения, которые в свою очередь делятся по категориям.
***
Для работы с проектом необходимо выполнить действия, описанные ниже.

git clone <project>
cd yamdb_final/infra/
Docker

docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic  
yes
docker-compose exec web python manage.py import_data  
Y
docker-compose exec web python manage.py createsuperuser
...  
> Superuser created successfully.
http://localhost/admin

Для получения документации по API необходимо открыть в браузере адрес http://localhost/redoc/.

GET http://localhost/api/v1/titles
GET http://localhost/api/v1/titles/1
GET http://localhost/api/v1/titles/1/reviews
GET http://localhost/api/v1/titles/5/reviews/6/comments
GET http://localhost/api/v1/titles/?year=1994
GET http://localhost/api/v1/titles/?genre=comedy

POSTMAN
Для полноценного использования API необходимо выполнить регистрацию пользователя и получить токен. Инструкция для Postman:

Регистрация пользователя
POST http://localhost/api/v1/auth/signup/

{
    "email": "tester1@mail.ru",
    "username": "tester1"
}
Response status 200 

{
    "username": "tester1",
    "email": "tester1@mail.ru"
}

Docker

docker-compose exec web ls sent_emails  
> Copy your file.log <20220603-081115-140473090362512.log>
docker-compose exec web cat sent_emails/<PASTE your file log>
> Код подтверждения: 61b-18466437bce...
POSTMAN
Получение токена POST http://localhost/api/v1/auth/token/

***
### Автор:
Мусиенко  -  - (https://github.com/AleksanderMoosieno)
