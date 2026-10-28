# Recuperer les bornes d'un fichier osm
# Code de Chatgpt

import xml.etree.ElementTree as ET

file_path = "map.osm"

tree = ET.parse(file_path)
root = tree.getroot()

bounds = root.find("bounds")

min_lat = float(bounds.attrib["minlat"])
min_lon = float(bounds.attrib["minlon"])
max_lat = float(bounds.attrib["maxlat"])
max_lon = float(bounds.attrib["maxlon"])

print("Latitude minimale :", min_lat)
print("Latitude maximale :", max_lat)
print("Longitude minimale :", min_lon)
print("Longitude maximale :", max_lon)

"""
Latitude minimale : 50.73421
Latitude maximale : 50.7457
Longitude minimale : 3.19558
Longitude maximale : 3.22927
"""
