# Insignts for Palmer Archipelago Penguins

[![Images Build and Push](https://github.com/teresaromero/palmer-penguins/actions/workflows/docker.yml/badge.svg?branch=development&event=push)](https://github.com/teresaromero/palmer-penguins/actions/workflows/docker.yml)
[![GitHub license](https://img.shields.io/github/license/teresaromero/palmer-penguins)](https://github.com/teresaromero/palmer-penguins/blob/development/LICENSE.md)

## About the Data

Data has been gathered from different sources listed below:

- [Kaggle Dataset](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data)
- [National Geographic](https://www.nationalgeographic.com/animals/birds/facts/gentoo-penguin)
- [National Geographic](https://www.nationalgeographic.com/animals/birds/facts/adelie-penguin)
- [National Geographic](https://www.nationalgeographic.com/animals/birds/facts/chinstrap-penguin)

## Motivation

The purpose for this project is educational. This project is the first of two to be done in the Data Bootcamp at :tangerine: [Core Code School](https://www.corecode.school/bootcamp/big-data-machine-learning).

Requirements for the project is to build a data app. This app should have a backend built with Flask, a frontend built with Streamlit and a database (Postgres or MongoDB).

## Services

The project has 3 main services: Database / API(backend) / Streamlit(frontend). Lets describe these services:

### :bar_chart: DATA

The data service is a custom mongodb image where the used data is added to the database in the init phase.

The original csv `source/penguins_lter.csv` is transformed into `database/docker-entrypoint-initdb.d/seed.json` by running `generate-seed-data.py`.

Once having the seed for the database, building the mongo image, `mongo-init.js` mongoshell script will create the admin and api users, and create the database with the different collections.

#### Collections

- `kaggle-raw-data`- the seed.json itself
- `ng-species-raw-data`- the species.json collection from web-scrapping NG
- `individuals` - collection with each penguin information regarding measures, each document has pointers to `islands`, `regions`, `species`, `studynames`
- `islands` - collection with the data regarding the island
- `regions` - collection with the data regarding the region
- `species` - collection with the data regarding the species
- `studynames` - collection with the data regarding the species

This collections are extracted from `kaggle-raw-data` in order to be able to include extra data for each collection without changing the `individuals` collection that is the main one.

### :gear: API

The API is a backend service for the streamlit frontend and the one that comunicates with the database. The sub-repo for the api is structured as follows:

- `main.py`- entry point for the flask server.
- `config.py`- env variables all in the same place.
- `routes`- dir with all the routes, entry point to the API.
- `controllers`- dir with the controllers for each route, responsible to exec the code for that route.
- `libs` - utils used along the project for different porpuses.
- `decorators` - custom decorator methods.

#### Routes

- `GET - /<collection>` - returns all the documents found for this collection on the database
- `PATCH - /<collection>/<id>` - modify the document `<id>` of the `<collection>`. The payload should be compliant with the collections fields.

#### Decorators

- `handle_error` - for each route, this decorator catches the errors and returns a json error response.
- `validate_route`- as root route is based on parameters, this decorator checks the collection exists at the db, if not it throws an error before accesing the controller.

#### Libs

- `mongo_client`- setup for the mongodb connection using `flask_pymongo`.
- `response`- utils to return different responses.

### :sparkles: STREAMLIT

This is the service where the data is displayed. This sub-repo is structured as following:

- `main.py` - entry point for the streamlit app
- `utils` - dir with methods used along the project
- `pages`- dir with the pages available in the streamlit app
- `components` - dir with the components used along the project
- `api` - dir with the methods used to call backend to retrieve data

#### Features

- Multi-page streamlit app
- Dashboard with data visualizations
- Edit database data
- Single page with species detail

## Usage

You can clone the repo and run `docker-compose up --build`.

### .ENV

Env variables needed to run the project

- `MONGO_URI` - uri for MongoDB DB (incl. db-name).
- `MONGO_DBNAME` - database name where all data will be stored.

- `MONGO_ADMIN_USERNAME` - username for the database admin user.
- `MONGO_ADMIN_PASSWORD` - password for the database admin user.

- `MONGO_API_USERNAME` - username for the database user used in the api.
- `MONGO_API_PASSWORD` - password for the database user used in the api.

- `FLASK_DEBUG` - flag to run Flask in debug mode, `False` or `True`.
- `FLASK_ENV` - environment where Flask is running, `development`.

- `API_URL` - url for the API.
- `API_PORT` - the port where the API will be available.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Stack

Flask, Streamlit, MongoDB, Docker
Pandas, PyMongo
Commitizen

## License

[MIT](https://choosealicense.com/licenses/mit/)
