# Verifier si un point est bien dans la carte
# Code fourni par ChatGPT

import xml.etree.ElementTree as ET
from pyproj import Transformer

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

# --- 5. Afficher les résultats ---
print(f"Longitude du point : {lon:.8f}")
print(f"Latitude du point  : {lat:.8f}")

print("\nBornes du fichier OSM :")
print(f"Longitude : {min_lon} à {max_lon}")
print(f"Latitude  : {min_lat} à {max_lat}")

if dans_le_cadre:
    print("\nOK : le point est dans le cadre OSM.")
else:
    print("\nATTENTION : le point est hors du cadre OSM.")
