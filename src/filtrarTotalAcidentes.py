import csv

def gerar_dados_gephi(arquivo_entrada, arquivo_nos, arquivo_arestas):
    id_counter = 1
    rodovia_ids = {}
    nos = []
    arestas = []

    with open(arquivo_entrada, mode='r', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)

        for linha in leitor:
            rodovia = linha[0]
            total = int(linha[1])
            graves = int(linha[2])
            feridos = int(linha[3])
            leves = int(linha[4])

            if rodovia not in rodovia_ids:
                rodovia_ids[rodovia] = id_counter
                nos.append([id_counter, rodovia, "Rodovia"])
                id_counter += 1

            rodovia_id = rodovia_ids[rodovia]

            caracteristicas = [
                ("Total de Acidentes", total),
                ("Acidentes Graves", graves),
                ("Acidentes com Feridos", feridos),
                ("Acidentes Leves", leves)
            ]

            for nome, valor in caracteristicas:
                if valor > 0:
                    caracteristica_id = id_counter
                    nos.append([caracteristica_id, f"{nome} ({rodovia})", nome])
                    id_counter += 1
                    arestas.append([rodovia_id, caracteristica_id, valor])

    with open(arquivo_nos, mode='w', encoding='utf-8', newline='') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(["Id", "Label", "Type"])
        escritor.writerows(nos)

    with open(arquivo_arestas, mode='w', encoding='utf-8', newline='') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(["Source", "Target", "Weight"])
        escritor.writerows(arestas)

arquivo_entrada = 'rodoviasAcidentes.csv'
arquivo_nos = 'gephi_nos.csv'
arquivo_arestas = 'gephi_arestas.csv'

gerar_dados_gephi(arquivo_entrada, arquivo_nos, arquivo_arestas)
