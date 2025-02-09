import csv

def criar_tabelas_gephi(arquivo_entrada, arquivo_arestas, arquivo_nos):
    try:
        with open(arquivo_entrada, mode='r', encoding='utf-8') as entrada:
            leitor = csv.reader(entrada, delimiter=',')
            cabecalho = next(leitor, None)
            
            if not cabecalho:
                print("Erro: O arquivo de entrada está vazio ou não possui cabeçalho.")
                return

            with open(arquivo_arestas, mode='w', encoding='utf-8', newline='') as saida_arestas, \
                 open(arquivo_nos, mode='w', encoding='utf-8', newline='') as saida_nos:

                escritor_arestas = csv.writer(saida_arestas, delimiter=',')
                escritor_nos = csv.writer(saida_nos, delimiter=',')

                escritor_nos.writerow(["Id", "Label", "Tipo"])
                escritor_arestas.writerow(["Source", "Target", "Relationship"])

                for linha in leitor:
                    try:
                        rodovia = linha[0].strip()
                        acidentes = int(linha[1])
                        graves = int(linha[2])
                        feridos = int(linha[3])
                        leves = int(linha[4])

                        escritor_nos.writerow([rodovia, rodovia, "Rodovia"])

                        id_acidentes = f"A_{rodovia}"
                        id_graves = f"G_{rodovia}"
                        id_feridos = f"F_{rodovia}"
                        id_leves = f"L_{rodovia}"

                        escritor_nos.writerow([id_acidentes, acidentes, "Acidentes"])
                        escritor_nos.writerow([id_graves, graves, "Graves"])
                        escritor_nos.writerow([id_feridos, feridos, "Feridos"])
                        escritor_nos.writerow([id_leves, leves, "Leves"])

                        escritor_arestas.writerow([rodovia, id_acidentes, "Acidentes"])
                        escritor_arestas.writerow([rodovia, id_graves, "Graves"])
                        escritor_arestas.writerow([rodovia, id_feridos, "Feridos"])
                        escritor_arestas.writerow([rodovia, id_leves, "Leves"])

                    except (ValueError, IndexError):
                        print(f"Erro ao processar linha: {linha}")

        print(f"Tabelas para Gephi criadas: {arquivo_arestas} e {arquivo_nos}.")

    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

criar_tabelas_gephi(
    "rodovias_acima_da_media.csv",
    "gephi_arestas_acima_media.csv",
    "gephi_nos_acima_media.csv"
)
