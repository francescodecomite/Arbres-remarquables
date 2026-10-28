import requests

url = "https://openstreetmap.org"

# CONFIGURATION DU USER-AGENT (À personnaliser obligatoirement)
headers = {
    'User-Agent': 'ArbresRemarquables/1.0 (fdecomite@gmail.com)'
}

response = requests.get(url, headers=headers)
print(response.status_code)

if response.status_code == 200:
    with open("tile.png", "wb") as f:
        f.write(response.content)



import folium

m = folium.Map(location=(45.5236, -122.6750))
m.save('index.html')

