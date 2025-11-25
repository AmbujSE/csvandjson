from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

#Examinw all the Earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# mags = []
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
print(len(all_eq_dicts))

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon= lons, title= title)
fig.show()