# shopalone
Shop alone! Tell others when you go and save lifes by avoiding queues &amp; crowds in times of Covid-19.

Wouldn't it be awesome to know when and where everyone else is shopping and simply go somewhere else?
Since such behaviour is mandatory to #flattenthecurve of corona-virus infections, *shopalone* tries to solve this issue.

With *shopalone*, users can enter when and where they are going for their groceries such that others can decide where to go based on the aggregated data.
All this is possible without sacrificing privacy of individuals - User accounts are not necessary and geodata is imported from OpenStreetMap.

## Project State
The 48 hours of the #wirvsvirus hackathon did not suffice to implement the full web service, but a first backend version serving a small REST-API works.
A minimal web frontend is work in progress, visualizations are still missing.
Feedback and contributions are highly welcome!

## Setup
- Clone this repository: `https://github.com/jvytee/shopalone.git`
- Download some OpenStreetMap data for your region, e.g. [here](https://download.geofabrik.de/) and place it in a subfolder called `data`
- Install [Osmosis](https://github.com/openstreetmap/osmosis) and setup a PostGIS database as lined out in the [documentation](https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup). You can use the supplied *docker-compose* setup to get a fresh PostgreSQL/PostGIS instance running in no time: `docker-compose up -d`
- Import data from your downloaded file into the database by executing `./import_osm.sh`
- Install python dependencies: `pip install -U -r requirements.txt`
- Set flask app: `export FLASK_APP=src/shopalone.py`
- Initialize the database: `flask init-db`
- Finally, start the API service: `flask run`

This process is not ideal; it will be improved after I had some sleep. Please do not use this setup in production!

## API Endpoints
All endpoints return JSON data.
- `/api/market?id=<market_id>`: Returns a single market
- `/api/market?postcode=<post_code>`: Returns all markets for a post code
- `/api/visit?market_id=>market_id>`: Returns all visits for a market
- `/api/visit` Sending `market_id` and `timestmap` via form data of a POST request adds a new visit and returns the visit object

## Web Frontennd
The web frontend can be accessed at `/web` or simply `/`. It should work with most browsers and does not require javascript.

![](Logo_Projekt_01.png)
