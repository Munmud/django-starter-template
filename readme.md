## About Us
- Team Name : `RU LEGION`
- Member1 : `Moontasir Mahmood` - `moontasir042@gmail.com`
- Member2 : `Md Atikur Rahman` - `md.atik.dev@gmail.com`
- Member3 : `Abdullah Al Ghalib` - `abdullah.ice.ru@gmail.com`

## Getting started

### Build Docker file
- `docker-compose build`

### To start project, run:
- `docker-compose up`


The API will then be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).


---
## Development Guide

### Load Initial Data
- `docker-compose run --rm app sh -c "python manage.py load_initial_books"`
- `docker-compose run --rm app sh -c "python manage.py generate_initial_super_user"`

### Create Project
- `docker-compose run app sh -c "django-admin startproject app ."`

### Create New App
- `docker-compose run app sh -c "python manage.py startapp core"`
- `docker-compose run --rm app sh -c "python manage.py startapp user"`
- `docker-compose run --rm app sh -c "python manage.py startapp book"`
- `docker-compose run --rm app sh -c "python manage.py startapp train"`

### Create Super User
- `docker-compose run --rm app sh -c "python manage.py createsuperuser"`

### Make Migrations
- `docker-compose run app sh -c "python manage.py makemigrations"`