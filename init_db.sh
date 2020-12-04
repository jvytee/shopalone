#!/bin/sh

if [ -z $3 ]; then
    echo "Usage: $0 <PostgreSQL host> <PostgreSQL port> <PostgreSQL database>"
    exit 0
fi

HOST=$1
PORT=$2
DATABASE=$3
USER=postgres
PASSWORD=postgres

psql -h $HOST -p $PORT -U $USER -c "CREATE DATABASE $DATABASE"
psql -h $HOST -p $PORT -U $USER -d $DATABASE -c "CREATE EXTENSION postgis; CREATE EXTENSION hstore;"
psql -h $HOST -p $PORT -U $USER -d $DATABASE -f pgsnapshot_schema_0.6.sql
