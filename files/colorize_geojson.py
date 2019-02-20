import json

file1 = open("current_ww.geojson")
data = json.load(file1)
file1.close()

for i in range(0, len(data['features'])):
    data['features'][i]['properties']['color'] = "#28B463"

json.dump(data, open('test.geojson','w'))
