import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'pink'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="stamen terrain")

fg=folium.FeatureGroup(name="My Map")

#Add a marker to the list
#fg.add_child(folium.Marker(location=[52.498466, -0.724506], popup="Hi I Live here", icon=folium.Icon(color=el)))

#To add multiple markers use a for loop

# for coordinates in [[52.498466, -0.724506], [51.398426, -0.723506]]:
#     fg.add_child(folium.(location=coordinates, popup="Hi I Live here", icon=folium.Icon(color="red")))

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color=color_producer(el),icon='any')))

# To use circle markers, use the code below

#for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=str(el), fill_color=color_producer(el),color ='gray',fill_opacity=0.7))



map.add_child(fg)



map.save("Map1.html")
print(data)


print(dir(folium))
help(folium.CircleMarker)

print(lon)