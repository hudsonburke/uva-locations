#! usr/bin/env python
# https://gis.stackexchange.com/questions/73756/is-it-possible-to-convert-regular-json-to-geojson
from sys import argv
from os.path import exists
import simplejson as json 

script, in_file, out_file = argv

data = json.load(open(in_file))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["Longitude"], d["Latitude"]],
            },
        "properties" : {
            "name": d["Name"],
            "address": d["Address"],
            "category": d["Category"]
        },
     } for d in data]
}

output = open(out_file, 'w')
json.dump(geojson, output)

print(geojson)
