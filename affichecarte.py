# ATTENTION : code fourni par ChatGPT. Mais ça marche
import geopandas as gpd
import matplotlib.pyplot as plt
import osmium

# 1. Charger les entités du fichier OSM (exemple avec les routes/ways)
# Remplacez 'votre_fichier.osm.pbf' par le chemin de votre fichier local
file_path = 'votre_fichier.osm.pbf'

fp = osmium.FileProcessor("./map.osm")\
    .with_locations()\
    .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))\
    .with_filter(osmium.filter.KeyFilter('highway'))\
    .with_filter(osmium.filter.GeoInterfaceFilter())

# Conversion en GeoDataFrame GeoPandas
gdf = gpd.GeoDataFrame.from_features(fp)

# 2. Re-projeter en Web Mercator (EPSG:3857) pour un bon affichage
gdf = gdf.set_crs(epsg=4326).to_crs(epsg=3857)

# 3. Afficher la carte avec Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, linewidth=0.5, color='blue')

plt.title('Carte générée depuis le fichier OSM local')
plt.show()
