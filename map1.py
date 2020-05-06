import folium
import pandas

data = pandas.read_csv("route-finder.csv")
data2 = pandas.read_csv("utby-all.csv")

lat = list(data["Area Latitude"])
lon = list(data["Area Longitude"])
route = list(data["Route"])
stars = list(data["Avg Stars"])

lat2 = list(data2["Area Latitude"])
lon2 = list(data2["Area Longitude"])
route2 = list(data2["Route"])
stars2 = list(data2["Avg Stars"])


def color_producer(score):
    if score < 2.0:
        return 'red'
    elif 2 <= score < 3.5:
        return 'orange'
    else:
        return 'green'


map = folium.Map(location=[57.741411, 12.06958],
                 zoom_start=13, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Some Routes")
fg2 = folium.FeatureGroup(name="Utby Routes")

for lt, ln, ro, sta in zip(lat, lon, route, stars):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6,
                                     popup=ro, fill_color=color_producer(sta), color='gray', fill=True, fill_opacity=0.5))

for lt, ln, ro, sta in zip(lat2, lon2, route2, stars2):
    fg2.add_child(folium.CircleMarker(location=[lt, ln], radius=6,
                                      popup=ro, fill_color=color_producer(sta), color='gray', fill=True, fill_opacity=0.5))

map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())

map.save("Map1.html")
