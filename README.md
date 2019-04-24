# Cleverbots

#### Deploy dev

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