#!/bin/sh

osmosis --read-pbf data/koeln-regbez-latest.osm.pbf \
    --tag-filter reject-relations \
    --tag-filter accept-nodes shop=convenience,general,supermarket \
    --tag-filter accept-ways shop=convenience,general,supermarket \
    --write-pgsql database=shopalone host=127.0.0.1 user=postgres password=postgres
