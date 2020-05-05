import folium
import pandas

data = pandas.read_csv("utby-all.csv")

lat = list(data["Area Latitude"])
lon = list(data["Area Longitude"])
route = list(data["Route"])
stars = list(data["Avg Stars"])


def color_producer(score):
    if score < 2.0:
        return 'red'
    elif 2 <= score < 3.5:
        return 'orange'
    else:
        return 'green'


map = folium.Map(location=[57.741411, 12.06958],
                 zoom_start=13, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Boulders")

for lt, ln, ro, sta in zip(lat, lon, route, stars):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=10,
                                     popup=ro, fill_color=color_producer(sta), color='gray', fill=True, fill_opacity=0.5))
map.add_child(fg)

map.save("Map1.html")
