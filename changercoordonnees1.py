from pyproj import Transformer

# Lambert 72 (EPSG:31370) -> WGS84 (EPSG:4326)
transformer = Transformer.from_crs(
    "EPSG:31370",
    "EPSG:4326",
    always_xy=True
)

x = 150000
y = 170000

lon, lat = transformer.transform(x, y)

print(f"Longitude : {lon:.8f}")
print(f"Latitude  : {lat:.8f}")
