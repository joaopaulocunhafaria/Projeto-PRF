import csv

def adicionar_coordenadas(arquivo_acidentes, arquivo_coordenadas, arquivo_saida):
    coordenadas = {}

    with open(arquivo_coordenadas, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)

        for linha in reader:
            rodovia = linha[0].strip()
            latitude = linha[1].strip().replace(",", ".")
            longitude = linha[2].strip().replace(",", ".")
            coordenadas[rodovia] = (latitude, longitude)

    with open(arquivo_acidentes, mode='r', encoding='utf-8') as file_acidentes, \
         open(arquivo_saida, mode='w', encoding='utf-8', newline='') as file_saida:

        reader = csv.reader(file_acidentes, delimiter=',')
        writer = csv.writer(file_saida, delimiter=',')

        cabecalho = next(reader)
        cabecalho.extend(["Latitude", "Longitude"])
        writer.writerow(cabecalho)

        for linha in reader:
            rodovia = linha[0].strip()
            if rodovia in coordenadas:
                linha.extend(coordenadas[rodovia])
            else:
                linha.extend(["", ""])
            writer.writerow(linha)

    print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

arquivo_acidentes = "rodovias_muito_acima_da_media.csv"
arquivo_coordenadas = "coordenadasRodovias.csv"
arquivo_saida = "rodovias_muito_acima_da_media_cordenadas.csv"

adicionar_coordenadas(arquivo_acidentes, arquivo_coordenadas, arquivo_saida)
