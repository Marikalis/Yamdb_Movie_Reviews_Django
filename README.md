
# YaMDb API Educational Project

![example workflow](https://github.com/Marikalis/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

The YaMDb project allows to add new users and collects user feedback on various movies.

### Author:
- Maria Lisitskaya https://github.com/Marikalis

### Technologies:
- Python
- Django
- PostgreSQL
- Docker, docker-compose
- Nginx used as a Webserver

### How to start the project:

Clone the repository and open it via the command line:

```
git clone https://github.com/Marikalis/api_yambd.git
cd api_yambd
```

Create and activate a virtual environment, install dependencies from the requirements.txt file, and perform migrations:

```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py migrate
```

If necessary, populate the database with test data:

1. Go to the root folder of the project where the csv_importer.py file is located.
2. Run the csv_importer.py script:
```
python3 csv_importer.py
```

Start the project:

```
python3 manage.py runserver
```

## API Documentation:

```
http://62.84.120.222/redoc/
```

Register a new user:

```
http://62.84.120.222/api/v1/auth/signup/
```

## Running Docker:

Start docker-compose:

```
docker-compose up -d --build
```

This will deploy the project running via Gunicorn with a PostgreSQL database. Perform migrations, create a superuser, populate the database with data, and collect static files:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py csv_importer.py
docker-compose exec web python manage.py collectstatic --no-input
```

Stopping containers and removing them along with all dependencies:

```
docker-compose down -v 
```

[Project address](http://62.84.120.222/redoc)

========================================================

# Учебный проект "YaMDb API"

![ example workflow ](https://github.com/Marikalis/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Проект YaMDb позволяет добавлять новых пользователей,
собирает отзывы пользователей на различные произведения.

### Автор:
- Maria Lisitskaya https://github.com/Marikalis

### Технологии:
- Python
- Django
- Posgresql
- Docker, docker-compose
- Nginx used as a Webserver

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Marikalis/api_yambd.git
cd api_yambd
```

Cоздать и активировать виртуальное окружение, установить зависимости из файла requirements.txt и выполнить миграции:

```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py migrate
```

Если необходимо, заполненить базу данных тестовыми данными:

1. перейдите в корневую папку проекта, где находится файл csv_importer.py
2. запустите скрипт csv_importer.py:
```
python3 csv_importer.py
```

Запустить проект:

```
python3 manage.py runserver
```

## Документация к API:

```
http://62.84.120.222/redoc/
```

Регистрация нового пользователя:

```
http://62.84.120.222/api/v1/auth/signup/
```

## Запуск Docker:

Запуcтить docker-compose:

```
docker-compose up -d --build
```

У вас развернется проект, запущенный через Gunicoren сбазой данных Postgres.
Выполнить миграции, создать суперпользователя и заполнить БД данными, а также собрать статику:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py csv_importer.py
docker-compose exec web python manage.py collectstatic --no-input
```

Остановка контейнеров и их удаление вместе со всеми зависимостями:

```
docker-compose down -v 
```

[Адрес проекта](http://62.84.120.222/redoc)
