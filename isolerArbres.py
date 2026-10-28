# Lire le fichier des arbres
# reperer toutes les lignes dont les coordonnées sont dans la carte
# Les sauver

import xml.etree.ElementTree as ET
from pyproj import Transformer
import numpy
import sys

# --- 1. Coordonnées du point en Lambert 72 ---
x_belge = 69133.3699999973
y_belge = 159913.017000001

# --- 2. Lire les bornes du fichier OSM ---
file_path = "map.osm"

tree = ET.parse(file_path)
root = tree.getroot()

bounds = root.find("bounds")

if bounds is None:
    raise ValueError("Aucune balise <bounds> trouvée dans map.osm")

min_lat = float(bounds.attrib["minlat"])
max_lat = float(bounds.attrib["maxlat"])
min_lon = float(bounds.attrib["minlon"])
max_lon = float(bounds.attrib["maxlon"])

print("latitude ", min_lat,",",max_lat)
print("longitude ", min_lon,",",max_lon)


# --- 3. Convertir Lambert 72 vers WGS84 ---
transformer = Transformer.from_crs(
    "EPSG:31370",
    "EPSG:4326",
    always_xy=True
)

lon, lat = transformer.transform(x_belge, y_belge)

# --- 4. Vérifier si le point est dans le cadre ---
dans_le_cadre = (
    min_lat <= lat <= max_lat
    and min_lon <= lon <= max_lon
)

lesarbres=open("./AHREM__ARBRES_31370.csv",encoding="cp1252", errors="ignore")
i=0
for ligne in lesarbres:
    i=i+1
    
    try:
        i=i+1
        u=ligne.split("POINT",1)[1][2:-2]
    except:
        print("Probleme ligne ", i)
        continue
    
    x,y=u.split(" ",1)
   
    try: 
        lon,lat=transformer.transform(x, y)
    except:
        #print(i," probleme ",ligne,"\n\t ",x,"\n\t ",y)
        continue
   
    dans_le_cadre = (
     min_lat <= lat <= max_lat
     and min_lon <= lon <= max_lon
     )
    if dans_le_cadre:
        #print("\t",x," ",y)
        print(i," ",lon," ",lat)

    
