# You can use a specific version too, like python:3.6.5-alpine3.7
# FROM python:3-alpine
FROM python:3.9.12-alpine
WORKDIR /usr/src/app
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps \
 gcc \
 python3-dev \
 musl-dev \
 postgresql-dev \
 && pip install --no-cache-dir psycopg2 \
 && apk del --no-cache .build-deps
RUN pip install -r requirements.txt

############
FROM postgres:latest
# Copy the SQL script to the container
COPY init.sql /docker-entrypoint-initdb.d/
# Set the POSTGRES_USER environment variable
ENV POSTGRES_USER myuser
# Set the POSTGRES_PASSWORD environment variable
ENV POSTGRES_PASSWORD mypassword
# Set the POSTGRES_DB environment variable
ENV POSTGRES_DB mydatabase
RUN apt-get update && apt-get install -y python3
RUN apt-get install python3-psycopg2
##########
COPY . .
CMD ["python3", "app.py"]