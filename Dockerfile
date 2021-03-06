FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code/
WORKDIR /code/
COPY requirements.txt /code/
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y gcc
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/
#RUN python3 manage.py migrate
#RUN python3 manage.py migrate

#EXPOSE 80
#CMD exec uwsgi --http 0.0.0.0:80 --module config.wsgi

