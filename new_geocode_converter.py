#! usr/bin/env python

from sys import argv
from os.path import exists
import simplejson as json 
import googlemaps
import string

script, in_file, out_file = argv

gmaps = googlemaps.Client(key=) #must insert own google maps API key
data = json.load(open(in_file))
geojson = {
    "type": "FeatureCollection",
    "features": [
    ]
}
for d in data:
    if d["Address"] == "" or not d["Address"][0].isnumeric():
        continue
    elif d["Longitude"] == None or d["Latitude"] == None:
        temp = gmaps.geocode(str(d["Address"]) + ' Charlottesville, VA')[0]['geometry']['location']
        coordinates = [temp['lng'], temp['lat']]
    else:
        coordinates = [d["Longitude"], d["Latitude"]]
    new_feature = {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": coordinates,
            },
        "properties" : {
            "name": string.capwords(d["Name"]),
            "address": d["Address"],
            "category": d["Category"]
        },
     }
    geojson["features"].append(new_feature)

output = open(out_file, 'w')
json.dump(geojson, output)

# print(geojson)
