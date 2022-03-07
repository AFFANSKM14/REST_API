import json
import csv
import requests
req=requests.get('https://data.police.uk/api/leicestershire/neighbourhoods')
req=req.json()
data_file = open('Neighbours.csv', 'w')
csv_writer = csv.writer(data_file)
header = req[0].keys()
csv_writer.writerow(header)
for r in req:
    csv_writer.writerow(r.values())
data_file.close()