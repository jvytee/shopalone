#!/bin/sh

DATA_PATH=data/koeln-regbez-latest.osm.pbf
DB_HOST=127.0.0.1
DB_USER=postgres
DB_PASSWORD=postgres

osmosis --read-pbf $DATA_PATH \
    --tag-filter reject-relations \
    --tag-filter accept-nodes shop=convenience,general,supermarket \
    --tag-filter accept-ways shop=convenience,general,supermarket \
    --write-pgsql database=shopalone host=$DB_HOST user=$DB_USER password=$DB_PASSWORD
