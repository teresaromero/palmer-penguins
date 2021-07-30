# CREATE JSON TO SEED INTO DATABASE
FROM python:3.9-slim-buster AS seeder

WORKDIR /usr/data

COPY . /usr/data/

RUN pip install -r /usr/data/requirements.txt

CMD [ "python", "generate-seed-data.py" ]

# USE MONGODB WITH JSON WHEN INIT
FROM mongo:latest

COPY --from=seeder /usr/data/database/docker-entrypoint-initdb.d /docker-entrypoint-initdb.d

EXPOSE 27017