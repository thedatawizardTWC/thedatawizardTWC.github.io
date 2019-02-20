import json

file1 = open("current_ww.geojson")
data = json.load(file1)
file1.close()

for i in range(0, len(data['features'])):
    ww = data['features'][i]['properties']['TYPE'] + data['features'][i]['properties']['SIG']
    if ww in ['FAA', 'FAY', 'FAW', 'FFS', 'FFA', 'FLY', 'FLW', 'FLA']:
        data['features'][i]['properties']['color'] = "#28B463"
    elif ww in ['WSW', 'WSA', 'WWY']:
        data['features'][i]['properties']['color'] = "#2876B4"
    else:
        data['features'][i]['properties']['color'] = "#ffffff"
        

json.dump(data, open('current_ww.geojson','w'))
