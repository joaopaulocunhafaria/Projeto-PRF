import csv

def calcular_media_acidentes(arquivo_csv):
    soma_acidentes = 0
    total_rodovias = 0

    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        for linha in reader:
            try:
                soma_acidentes += int(linha[1])
                total_rodovias += 1
            except (ValueError, IndexError):
                print(f"Erro ao processar linha: {linha}")

    if total_rodovias == 0:
        return 0

    print (f"Total de rodovias: {total_rodovias}")
    print (f"Total de acidentes: {soma_acidentes}")
    media = soma_acidentes / total_rodovias
    return media

arquivo = "rodoviasAcidentes.csv"
media_acidentes = calcular_media_acidentes(arquivo)
print(f"Média de acidentes por rodovia: {media_acidentes:.2f}")
