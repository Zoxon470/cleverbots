# Cleverbots

Test assignment for cleverbots.ru

#####1. Постановка задачи

Разработать REST API сервер для хранения фотографий. Сервер предпо-
лагает наличие двух запросов, с помощью которых можно будет отправлять
для хранения фотографии и просматривать все добавленные ранее фото-
графии. Помимо запросов требуется реализовать панель администратора,
в которой можно просматривать добавленные фотографии.

#####2.  Пожелания

1. Framework - Django
2. Database - Postgres
3. Покрытие тестами двух REST запросов
4. Наличие инструкции для деплоя на сервере
5. Панель администратора - django admin
6. REST API - django rest framework
7. Выложить на github

#####3. API описание

У сервера будет два REST запроса (Таб. 1):
1. Добавление фотографий в систему
2. Выгрузка информации по всем загруженным фотографиям

Method | Request | Parameters | Response
------------ | ------------- | ------------ | ------------- 
GET | Photos | Параметры для фильтрации: {"date": <string>, "size": <int>} | 200 [{ "date": <string> "place": <string>, "path_to_img": <string> }] | 
POST | Photo | { "place": <string>, "img": <формат по желанию> } | 200 

Таб. 1

#### Run dev

```sh
$ git clone https://github.com/Zoxon470/cleverbots
$ cd cleverbots
$ nano .env.local # see .env.example for example envs
$ docker-compose -f dev.yml up --build # building and running containers
```

#### Run tests

```sh
$ docker exec -i cleverbots-backend ./manage.py test upload.tests
```
