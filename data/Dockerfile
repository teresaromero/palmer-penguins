# CREATE JSON TO SEED INTO DATABASE
FROM python AS seeder

WORKDIR /usr/data

COPY . /usr/data/

CMD [ "python", "generate-seed-data.py" ]

# USE MONGODB WITH JSON WHEN INIT
FROM mongo:latest

COPY --from=seeder /usr/data/database/docker-entrypoint-initdb.d /docker-entrypoint-initdb.d

EXPOSE 27017