import csv
import folium
from shapely.geometry import Point

# Caminho para o arquivo CSV
csv_file_path = "acidentes2024_todas_causas_tipos.csv"

# Inicializa o mapa centralizado no Brasil
mymap = folium.Map(location=[-14.2350, -51.9253], zoom_start=4, tiles="OpenStreetMap")

# Lista para armazenar as coordenadas das linhas relevantes
coordinates = []

# Abre o arquivo CSV com a codificação apropriada e lê as coordenadas
with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    next(csvreader)  # Pula o cabeçalho, se houver

    for row in csvreader:
        try:
            # Verifica se a linha contém "Com Vítimas Fatais" na 14ª posição (índice 13)
            if row[13].strip() == "Com VÃ­timas Fatais":
                #print(row[13].strip())
                # Converte latitude e longitude do formato com vírgula para ponto
                lat = float(row[32].replace(",", "."))  # Coluna 32 (índice 31)
                lon = float(row[33].replace(",", "."))  # Coluna 33 (índice 32)
                print(lat, lon)
                coordinates.append([lat, lon])
        except (ValueError, IndexError):
            #print(f"Linha inválida ignorada: {row}")
            continue

# Se coordenadas foram encontradas, recentra o mapa na primeira coordenada
if coordinates:
    mymap.location = coordinates[0]
    mymap.zoom_start = 12  # Ajusta o nível de zoom conforme necessário

# Plota cada coordenada como um ponto vermelho no mapa
for coord in coordinates:
    folium.CircleMarker(
        location=coord,
        radius=3,               # Tamanho do ponto
        color='red',            # Cor da borda
        fill=True,
        fill_color='red',       # Cor do preenchimento
        fill_opacity=1          # Opacidade do preenchimento
    ).add_to(mymap)

# Salva o mapa como um arquivo HTML
output_file = "fatalAccidentsMap.html"
mymap.save(output_file)
print(f"Mapa com pontos vermelhos salvo como {output_file}")
