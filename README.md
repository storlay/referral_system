<h1 align="center">API: Простая реферальная система 🤝</h1>

<div align="center">

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/django_rest_framework-0C4B33?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Postgres](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)](https://python-poetry.org/)


</div>

Выполнено в рамках [тестового задания](https://storlay.notion.site/Python-681fde777730494f8d69c64c7f756a8b)

## Установка и запуск:

1. Склонируйте репозиторий

```
git clone https://github.com/storlay/referral_system.git
```

2. В корневой папке проекта создайте и заполните файл .env:

```
SECRET_KEY=your_secret_key

POSTGRES_ENGINE=django.db.backends.postgresql_psycopg2
POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=your_port
```

3. Запустите проект c помощью Docker:

```
docker-compose up --build
```

4. Приложение будет доступно по адресу http://127.0.0.1:8000

## Использование

Документация API доступна по адресу:

- http://127.0.0.1:8000/api/schema/redoc/ (Redoc)