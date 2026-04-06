import json
from shapely.geometry import shape

# path boundary.geojson
GEOJSON_PATH = r"C:\path\to\boundary.geojson"

with open(GEOJSON_PATH) as f:
    data = json.load(f)


if data["type"] == "FeatureCollection":
    geometry = data["features"][0]["geometry"]
elif data["type"] == "Feature":
    geometry = data["geometry"]
else:
    geometry = data  

polygon = shape(geometry)
centroid = polygon.centroid
bbox = polygon.bounds 

print("===== COPY THESE VALUES INTO YOUR APP =====")
print(f"CENTROID_LAT = {centroid.y}")
print(f"CENTROID_LNG = {centroid.x}")
print(f"BBOX_MIN_LON = {bbox[0]}")
print(f"BBOX_MIN_LAT = {bbox[1]}")
print(f"BBOX_MAX_LON = {bbox[2]}")
print(f"BBOX_MAX_LAT = {bbox[3]}")
print("===========================================")
