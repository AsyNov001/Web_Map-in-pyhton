import pandas as pd
import folium as f

M = f.Map(location = [26.01,97.0101],tiles = "Mapbox Bright",zoom_start = 11)
Data = pd.read_csv("Volcanoes_USA.txt")

Lat = list(Data["LAT"])
Lon = list(Data["LON"])
Elev = list(Data["ELEV"])
Name = list(Data["NAME"])

def encoder(Elev):
    if(Elev < 1000):
        return "green"
    elif(Elev > 1000)&(Elev < 2000 ):
        return "orange"
    else:
        return "red"

MA1 = f.FeatureGroup(name = "Volcanoes")
MA2 = f.FeatureGroup(name = "Population")

for i,j,k,m in zip(Lat,Lon,Elev,Name):
    MA1.add_child(f.Marker(location = [i,j],popup = str(m) + str(k) + "m",icon = f.Icon(color = encoder(k))))

MA2.add_child(f.GeoJson(data = open("world.json","r",encoding = "utf-8-sig").read(),style_function =
lambda x:{"fillColor":"green" if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

M.add_child(MA1)
M.add_child(MA2)
M.add_child(f.LayerControl())

M.save("Map.html")
