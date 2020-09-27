# shopalone
Shop alone! Tell others when you go and save lifes by avoiding queues &amp; crowds in times of Covid-19.

Wouldn't it be awesome to know when and where everyone else is shopping and simply go somewhere else?
Since such behaviour is mandatory to #flattenthecurve of corona-virus infections, *shopalone* tries to solve this issue.

With *shopalone*, users can enter when and where they are going for their groceries such that others can decide where to go based on the aggregated data.
All this is possible without sacrificing privacy of individuals - User accounts are not necessary and geodata is imported from OpenStreetMap.

## Project State
The 48 hours of the #wirvsvirus hackathon did not suffice to implement the full web service, so only a prototype backend serving a small REST-API could be realized.
A minimal web frontend was added eventually.

## Installation
- Download some OpenStreetMap data as PBF file for your region, e.g. from [here](https://download.geofabrik.de/) 
- Install [Osmosis](https://github.com/openstreetmap/osmosis) and setup a PostGIS database as lined out in the [documentation](https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup). The `postgis/postgis` Docker image provides an easy way to get a PostGIS database running quickly.
- Clone this repository: `https://github.com/jvytee/shopalone.git`
- Import data from your downloaded file into the database by executing `./import_osm.sh <PBF path> <PostgreSQL host> <PostgreSQL schema>`
- Install *shopalone* and dependencies: `pip install .`
- Set *shopalone* as Flask app: `export FLASK_APP=shopalone.main:app`
- Initialize the database: `flask init-db`

## Running
For development and debugging purposes, the service can be started by `flask run`.
In a production environment however, the service should be run with an application server such as [Gunicorn](https://gunicorn.org/).

For a containerized setup, the provided `Dockerfile` and `docker-compose.yml` can serve as a reference.

## Endpoints
All API endpoints return JSON data, the web frontend is plain HTML.
- `/api/market?id=<market_id>`: Returns a single market
- `/api/market?postcode=<post_code>`: Returns all markets for a post code
- `/api/visit?market_id=<market_id>`: Returns all visits for a market
- `/api/visit` Sending `market_id` and `timestmap` via form data of a POST request adds a new visit and returns the visit object
- `/web` Serves as entry to the web frontend

![](Logo_Projekt_01.png)
