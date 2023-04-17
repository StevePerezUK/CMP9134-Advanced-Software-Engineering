FROM postgres:latest
COPY init.sql /docker-entrypoint-initdb.d/
RUN chmod 0777 /docker-entrypoint-initdb.d/init.sql
