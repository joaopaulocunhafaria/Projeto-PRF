import csv
import folium
import geopandas as gpd
from shapely.geometry import Point

csv_file_path = "rodovias_muito_acima_da_media_cordenadas.csv"
 
mymap = folium.Map(location=[-14.2350, -51.9253], zoom_start=4, tiles="OpenStreetMap")
 
coordinates = []

with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        try:
            lat = float(row[5].replace(",", "."))
            lon = float(row[6].replace(",", "."))
            point = Point(lon, lat)
            coordinates.append([lat, lon])
        except (ValueError, IndexError):
            print(f"Skipping invalid row: {row}")
            continue

if coordinates:
    mymap.location = coordinates[0]
    mymap.zoom_start = 12

for coord in coordinates:
    folium.CircleMarker(
        location=coord,
        radius=7,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=1
    ).add_to(mymap)

output_file = "rodoviasMuitoAcimaMedia.html"
mymap.save(output_file)
print(f"Map with red dots saved as {output_file}")
