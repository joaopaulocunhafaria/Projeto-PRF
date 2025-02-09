import csv
import folium
from shapely.geometry import Point

csv_file_path = "acidentes2024_todas_causas_tipos.csv"

mymap = folium.Map(location=[-14.2350, -51.9253], zoom_start=4, tiles="OpenStreetMap")

coordinates = []

with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    next(csvreader)

    for row in csvreader:
        try:
            if row[13].strip() == "Com VÃ­timas Fatais":
                lat = float(row[32].replace(",", "."))
                lon = float(row[33].replace(",", "."))
                coordinates.append([lat, lon])
        except (ValueError, IndexError):
            continue

if coordinates:
    mymap.location = coordinates[0]
    mymap.zoom_start = 12

for coord in coordinates:
    folium.CircleMarker(
        location=coord,
        radius=3,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=1
    ).add_to(mymap)

output_file = "fatalAccidentsMap.html"
mymap.save(output_file)
print(f"Mapa com pontos vermelhos salvo como {output_file}")
