import csv

def filtrar_acima_da_media(arquivo_entrada, arquivo_saida, media_acidentes):
    with open(arquivo_entrada, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        with open(arquivo_saida, mode='w', encoding='utf-8', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)

            for linha in reader:
                try:
                    numero_acidentes = int(linha[1])
                    if numero_acidentes > media_acidentes:
                        writer.writerow(linha)

                except (ValueError, IndexError):
                    print(f"Erro ao processar linha: {linha}")

arquivo_entrada = "rodoviasAcidentes.csv"
arquivo_saida = "rodovias_muito_acima_da_media.csv"
media_acidentes = 10000

filtrar_acima_da_media(arquivo_entrada, arquivo_saida, media_acidentes)

print(f"Arquivo {arquivo_saida} gerado com sucesso!")
