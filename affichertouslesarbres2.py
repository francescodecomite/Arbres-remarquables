# ATTENTION : code fourni par ChatGPT. Mais ça marche

# Les coordonnées de tous les arbres visibles sur la carte sont
# dans le fichier coordonnees.txt
# une ligne reprenant toutes les infos de la feuille de classeur
# Suivie d'une ligne ne contenant que trois nombres :
# Le numéro de la ligne du fichier initial (à vérifier)
# et la longitude et la latitude

import geopandas as gpd
import matplotlib.pyplot as plt
import osmium
import re

file_path = 'map4.osm'  # Remplacez par le chemin de votre fichier

# --- 1. EXTRACTION DES ENTIÈRES DU FICHIER ---
# On extrait tous les "Ways" (lignes et polygones) qui possèdent des propriétés (tags)
fp = osmium.FileProcessor(file_path)\
    .with_locations()\
    .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))\
    .with_filter(osmium.filter.GeoInterfaceFilter())

# Conversion globale en GeoDataFrame GeoPandas
gdf_global = gpd.GeoDataFrame.from_features(fp)

# Si le fichier est vide ou mal lu, on s'arrête
if gdf_global.empty:
    print("Aucune donnée trouvée dans le fichier OSM.")
    exit()

# Définir le système de coordonnées initial (WGS84) puis projeter en Web Mercator pour l'affichage
gdf_global = gdf_global.set_crs(epsg=4326).to_crs(epsg=3857)

# --- 2. FILTRAGE SIMPLE AVEC GEOPANDAS ---

# Les colonnes de votre GeoDataFrame correspondent aux tags OSM (ex: highway, building, leisure...)
# On vérifie si les colonnes existent avant de filtrer pour éviter de faire planter le code

# Filtrer les routes
gdf_routes = gdf_global[gdf_global['highway'].notna()] if 'highway' in gdf_global.columns else gpd.GeoDataFrame()

# Filtrer les bâtiments
gdf_buildings = gdf_global[gdf_global['building'].notna()] if 'building' in gdf_global.columns else gpd.GeoDataFrame()

# Filtrer UNIQUEMENT les parcs (Équivalent de votre ancien KeyValueFilter)
gdf_parks = gpd.GeoDataFrame()
if 'leisure' in gdf_global.columns:
    gdf_parks = gdf_global[gdf_global['leisure'] == 'park']

# --- 3. AFFICHAGE DES COUCHES ---

fig, ax = plt.subplots(figsize=(60, 60))

# Dessiner les parcs (arrière-plan)
if not gdf_parks.empty:
    gdf_parks.plot(ax=ax, color='#a1dbb2', alpha=0.7)

# Dessiner les bâtiments
if not gdf_buildings.empty:
    gdf_buildings.plot(ax=ax, color='#d3d3d3', edgecolor='#a9a9a9', linewidth=0.5)

# Dessiner les routes (au-dessus)
if not gdf_routes.empty:
    gdf_routes.plot(ax=ax, color='#f1a340', linewidth=0.8)

# Insertion Chatgpt
from shapely.geometry import Point






lesarbres=open("coordonnees2.txt")
i=0
for ligne in lesarbres :
    i=i+1
    if i%2==1:
        continue

    s = ligne
    matches = re.findall(r'-?\d*\.?\d+', s)
    res = [float(x) if '.' in x else int(x) for x in matches]
    print(res)


    # Création du point dans le système belge Lambert 72
    gdf_point = gpd.GeoDataFrame(
        {'nom': ['Mon point']},
        geometry=[Point(res[1], res[2])],
        crs='EPSG:31370'
    )

    # Conversion vers le système de coordonnées de la carte
    gdf_point = gdf_point.to_crs(epsg=3857)

    # Affichage du point sur la carte
    gdf_point.plot(
        ax=ax,
        color='red',
        markersize=40,
        marker='o',
        edgecolor='black'
    )

    # Affichage du nom du point
    x = gdf_point.geometry.iloc[0].x
    y = gdf_point.geometry.iloc[0].y

    ax.annotate(
        str(res[0]),
        xy=(x, y),
        xytext=(5, 5),
        textcoords='offset points',
        color='red',
        fontsize=5
    )
# Fin insertion chatgpt
ax.set_axis_off()
plt.title('Carte OSM filtrée avec GeoPandas')

plt.savefig('./parc.jpg')
#plt.show()

