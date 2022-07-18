# CI и CD проекта api_yamdb
***
![workflow](https://github.com/AleksanderMoosieno/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# API_YaMDB
***
### __Описание__
***
#### Технологии:
1. [Django](https://www.djangoproject.com)
2. [Django Rest Framework](https://www.django-rest-framework.org)
3. SQlite
4. JWT авторизация

__API__ стремится к __RESTFUL__ и представляет собой проект, который собирает отзывы
на произведения, которые в свою очередь делятся по категориям.
***
#### Эндпоинты
* /redoc/ - Документация
* /api/v1/auth/signup/ - Создание пользователя(получение кода подтверждения)
* /api/v1/auth/token/ - Получение токена
* /api/v1/categories/ - Получение списка категорий 
* /api/v1/genres/ - Получение списка жанров
* /api/v1/titles/ - Получение списка произведений
* /api/v1/titles/{id}/ - Подробная информация
* /api/v1/titles/{title_id}/reviews/ - Посмотреть || Добавить отзывы
* /api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Посмотреть || Добавить комментарии к отзыву
* /api/v1/users/me/ - Информация о вашем аккаунте

***
### Для развёртывания:
Как запустить проект на Docker
Запустить проект при скачанном образе api_yamdb последней версии:

docker run api_yamdb
Создать и активировать виртуальное окружение:

source venv/bin/activate
После поочереди выполните команды:

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input

Заполнение баз данных, выполнить локально, данные сохранятся в dump.json:

python manage.py dumpdata > dump.json

***
### Автор:
Мусиенко Александр - работы - (https://github.com/AleksanderMoosieno)
Открываем браузер, вводим в адресную строку <ip_address_вашего_сервера>/api/v/
