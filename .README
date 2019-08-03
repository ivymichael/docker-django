# Dockerized Django
> docker + django + nginx + postgres + gunicorn

## Setup

# Dev
docker-compose up -d --build 

# Production (nginx and gunicorn added)
docker-compose -f docker-compose.prod.yml  up -d --build

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear 


# Reference

