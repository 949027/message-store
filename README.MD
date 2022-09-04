# Сервис хранения сообщений
- генерирует токен для авторизации;
- хранит сообщения от пользователей;
- направляет пользователю его историю сообщений.

Бэкенд - Django, Django RFW.

БД - Postgres.


## Запуск в Docker
1) Установите [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/).
2) Скачайте проект:
```commandline
git clone https://github.com/949027/message-store
```
3) Создайте файл `.env` в корне проекта со следующими настройками.

Необходимо:
- `POSTGRES_USER` - имя пользователя БД;
- `POSTGRES_PASSWORD` - пароль пользователя БД;
- `SECRET_KEY` — [секретный ключ](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECRET_KEY) проекта. Он отвечает за шифрование на сайте

Необязательно:
- `DEBUG` - [дебаг-режим](https://docs.djangoproject.com/en/4.1/ref/settings/#debug). По умолчанию - True.
- `ALLOWED_HOSTS` - [список допустимых хостов](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts). По умолчанию - 127.0.0.1, localhost.

4) Соберите и запустите контейнеры:
```commandline
docker-compose up
```

5) В другом терминале создайте суперпользователя:
```commandline
docker exec -it django python manage.py createsuperuser
```
6) После этого можно использовать админ-панель http://127.0.0.1:8000/admin/ и добавить ещё пользователей.

## Как использовать
### Получить токен для авторизации
Отправить post-запрос на http://127.0.0.1:8000/app/token/ с `username` и `password` пользователя в теле запроса (можно использовать данные при создании суперпользователя).
```commandline
curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' http://127.0.0.1:8000/app/token/
```
### Сохранить сообщение в БД
Отправить post-запрос на http://127.0.0.1:8000/app/message/ с `Authorization` в заголовке и `message` в теле запроса:
```commandline
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer_token" -d '{"message": "Hello"}' http://127.0.0.1:8000/app/message/
```
где token - заранее полученный токен 
### Получить историю сообщений
Отправить post-запрос на http://127.0.0.1:8000/app/message/ с `Authorization` в заголовке и `message` (вида `history {amount}`) в теле запроса:
```commandline
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer_token" -d '{"message": "history 10"}' http://127.0.0.1:8000/app/message/
```
где token - заранее полученный токен.

Выводит последние 10 сообщений.

## Цели проекта
Код написан в качестве тестового задания.