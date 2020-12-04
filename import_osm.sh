#!/bin/sh

if [ -z $3 ]; then
    echo "Usage: $0 <PBF path> <PostgreSQL host> <PostgreSQL database>"
    exit 0
fi

DATA_PATH=$1
DB_HOST=$2
DB_DATABASE=$3
DB_USER=postgres
DB_PASSWORD=postgres

osmosis --read-pbf $DATA_PATH \
    --tag-filter reject-relations \
    --tag-filter accept-nodes shop=convenience,general,supermarket \
    --tag-filter accept-ways shop=convenience,general,supermarket \
    --write-pgsql database=$DB_DATABASE host=$DB_HOST user=$DB_USER password=$DB_PASSWORD
