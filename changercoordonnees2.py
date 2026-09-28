from pyproj import Transformer

transformer = Transformer.from_crs(
    31370,
    4326,
    always_xy=True
)

points = [
    (150000, 170000),
    (100000, 200000),
    (200000, 150000),
]

for x, y in points:
    lon, lat = transformer.transform(x, y)
    print(f"{x}, {y} -> {lon:.8f}, {lat:.8f}")
