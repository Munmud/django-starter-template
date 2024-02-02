## Getting started

### Build Docker file
- `docker-compose build`

To start project, run:

```cmd
docker-compose up
```

The API will then be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).


---
## Development Guide

### Load Initial Products
- `docker-compose run --rm app sh -c "python manage.py load_initial_products"`
- `docker-compose run --rm app sh -c "python manage.py load_initial_books"`

### Create Project
- `docker-compose run app sh -c "django-admin startproject app ."`

### Create New App
- `docker-compose run app sh -c "python manage.py startapp core"`
- `docker-compose run --rm app sh -c "python manage.py startapp user"`
- `docker-compose run --rm app sh -c "python manage.py startapp book"`

### Create Super User
- `docker-compose run --rm app sh -c "python manage.py createsuperuser"`

### Make Migrations
- `docker-compose run app sh -c "python manage.py makemigrations"`