import json


with open('/Users/antropoloops/Desktop/antropoloops/Box Sync/VIZ/1_BDatos/BDlugares_mundo.txt') as f:
    json_data = json.load(f)

for place in json_data:
    country = place['lugar']
    if len(country) > 15:
        print(country)