import geopandas as gpd
import matplotlib.subplots as plt
import osmium
from shapely.geometry import Point  # <--- Import nécessaire pour créer le point

file_path = 'votre_fichier.osm.pbf'  # Remplacez par le chemin de votre fichier

# --- 1. CONFIGURATION DU POINT PERSO ---
# Remplacez par vos coordonnées (Attention : Longitude d'abord, Latitude ensuite)
ma_longitude = 2.3522   # Exemple : Paris
ma_latitude = 48.8566

# Création du point avec GeoPandas
point_geom = Point(ma_longitude, ma_latitude)
gdf_mon_point = gpd.GeoDataFrame(geometry=[point_geom], crs="EPSG:4326")
gdf_mon_point = gdf_mon_point.to_crs(epsg=3857)  # Alignement sur le repère de la carte


# --- 2. EXTRACTION DES DONNÉES OSM ---
fp = osmium.FileProcessor(file_path)\
    .with_locations()\
    .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))\
    .with_filter(osmium.filter.GeoInterfaceFilter())

gdf_global = gpd.GeoDataFrame.from_features(fp)

if gdf_global.empty:
    print("Aucune donnée trouvée dans le fichier OSM.")
    exit()

gdf_global = gdf_global.set_crs(epsg=4326).to_crs(epsg=3857)


# --- 3. FILTRAGE DES COUCHES ---
gdf_routes = gdf_global[gdf_global['highway'].notna()] if 'highway' in gdf_global.columns else gpd.GeoDataFrame()
gdf_buildings = gdf_global[gdf_global['building'].notna()] if 'building' in gdf_global.columns else gpd.GeoDataFrame()


# --- 4. AFFICHAGE DES COUCHES ET DU POINT ---
fig, ax = plt.subplots(figsize=(12, 12))

# Dessiner les bâtiments
if not gdf_buildings.empty:
    gdf_buildings.plot(ax=ax, color='#d3d3d3', edgecolor='#a9a9a9', linewidth=0.5)

# Dessiner les routes
if not gdf_routes.empty:
    gdf_routes.plot(ax=ax, color='#f1a340', linewidth=0.8)

# --- DESSINER LE POINT PERSO (Tout au-dessus) ---
gdf_mon_point.plot(
    ax=ax, 
    color='red',          # Couleur du point
    markersize=150,       # Taille du point
    marker='o',           # Forme (ici un cercle)
    edgecolor='black',    # Contour du point pour le faire ressortir
    zorder=5              # S'assure que le point se dessine au-dessus de tout
)

# Optionnel : Ajouter un texte à côté du point
ax.text(
    gdf_mon_point.geometry.iloc[0].x + 50,  # Décalage léger en X (en mètres)
    gdf_mon_point.geometry.iloc[0].y + 50,  # Décalage léger en Y (en mètres)
    "Mon Point Perso", 
    color='black', 
    fontsize=12, 
    weight='bold'
)

ax.set_axis_off()
plt.title('Carte OSM avec un repère personnalisé')
plt.show()
