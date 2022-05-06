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
```

```
cd api_yambd
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
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
http://127.0.0.1:8000/redoc/
```

Регистрация нового пользователя:

```
http://127.0.0.1:8000/api/v1/auth/signup/
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

### Адрес проекта:

```
http://62.84.120.222/admin/login/?next=/admin/ 
```