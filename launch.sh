#!/bin/sh

# Example setup for application deployment.
# While this script uses Podman to mangage containers, the command can be
# sustituded with Docker if needed.

echo Launching PostGIS container
sudo podman run --rm --name shopalone-postgis -d -e POSTGRES_PASSWORD=postgres -p 127.0.0.1:5432:5432 -v $(pwd)/data/postgres:/var/lib/postgresql/data postgis/postgis

echo -e "\nStarting Gunicorn application server"
cd src
gunicorn -w 2 shopalone:app

echo -e "\nStopping PostGIS container"
sudo podman stop shopalone-postgis
