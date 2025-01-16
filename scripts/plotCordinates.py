import csv
import folium
import geopandas as gpd
from shapely.geometry import Point

# Set the path to your CSV file and the GeoJSON file
csv_file_path = "acidentes2024_capitais.csv"
 
# Initialize the map centered on Brazil
mymap = folium.Map(location=[-14.2350, -51.9253], zoom_start=4, tiles="OpenStreetMap")
 
# Initialize a list to store coordinates
coordinates = []

# Open the CSV file with a specific encoding and read coordinates from columns 31 (latitude) and 32 (longitude)
with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:  # Specify encoding here
    csvreader = csv.reader(csvfile, delimiter=';')
    next(csvreader)  # Skip the header row if there is one

    for row in csvreader:
        try:
            # Convert latitude and longitude from comma format to dot format
            lat = float(row[32].replace(",", "."))  # Column 31 (zero-indexed as 30)
            lon = float(row[33].replace(",", "."))  # Column 32 (zero-indexed as 31)
            point = Point(lon, lat)  # Create a point from longitude and latitude

            # Check if the point is in Brazil
            
            coordinates.append([lat, lon])
        except (ValueError, IndexError):
            print(f"Skipping invalid row: {row}")
            continue

# If coordinates were found, re-center the map on the first coordinate
if coordinates:
    mymap.location = coordinates[0]
    mymap.zoom_start = 12  # Adjust zoom level as needed

# Plot each coordinate as a red dot on the map
for coord in coordinates:
    folium.CircleMarker(
        location=coord,
        radius=3,               # Size of the dot
        color='red',            # Outline color
        fill=True,
        fill_color='red',       # Fill color
        fill_opacity=1          # Opacity of the fill
    ).add_to(mymap)

# Save the map as an HTML file
output_file = "capitalsAcidents.html"
mymap.save(output_file)
print(f"Map with red dots saved as {output_file}")
