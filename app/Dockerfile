FROM python:3

#set work dir
WORKDIR /home/src/app

# set env
# do not store .pyc file
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
# install python dependencies
RUN pip install --upgrade pip \
    && pip install pipenv psycopg2

COPY ./Pipfile /home/src/app/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy entrypoint.sh
COPY ./entrypoint.sh /home/src/app/entrypoint.sh

# copy project
COPY . /home/src/app/

# run entrypoint.sh
ENTRYPOINT ["/home/src/app/entrypoint.sh"]