import csv

def criar_tabelas_gephi(arquivo_entrada, arquivo_arestas, arquivo_nos):
    try:
        with open(arquivo_entrada, mode='r', encoding='utf-8') as entrada:
            leitor = csv.reader(entrada, delimiter=';')
            cabecalho = next(leitor, None)
            if not cabecalho:
                print("Erro: O arquivo de entrada está vazio ou não possui cabeçalho.")
                return
            indices = {
                "id": cabecalho.index("id"),
                "classificacao_acidente": cabecalho.index("classificacao_acidente"),
                "ano_fabricacao_veiculo": cabecalho.index("ano_fabricacao_veiculo"),
                "marca": cabecalho.index("marca"),
            }
            with open(arquivo_arestas, mode='w', encoding='utf-8', newline='') as saida_arestas:
                with open(arquivo_nos, mode='w', encoding='utf-8', newline='') as saida_nos:
                    escritor_arestas = csv.writer(saida_arestas, delimiter=';')
                    escritor_nos = csv.writer(saida_nos, delimiter=';')
                    escritor_arestas.writerow(["Source", "Target", "Relationship"])
                    escritor_nos.writerow(["Id", "Label", "Category"])
                    nos = set()
                    for linha in leitor:
                        id_acidente = linha[indices["id"]]
                        classificacao_acidente = linha[indices["classificacao_acidente"]]
                        ano_fabricacao_veiculo = linha[indices["ano_fabricacao_veiculo"]]
                        marca = linha[indices["marca"]]
                        if ano_fabricacao_veiculo not in nos:
                            escritor_nos.writerow([ano_fabricacao_veiculo, ano_fabricacao_veiculo, "Ano de Fabricação"])
                            nos.add(ano_fabricacao_veiculo)
                        if marca not in nos:
                            escritor_nos.writerow([marca, "", "Marca"])
                            nos.add(marca)
                        if classificacao_acidente not in nos:
                            escritor_nos.writerow([classificacao_acidente, "", "Classificação do Acidente"])
                            nos.add(classificacao_acidente)
                        escritor_arestas.writerow([ano_fabricacao_veiculo, marca, "Relacionado"])
                        escritor_arestas.writerow([ano_fabricacao_veiculo, classificacao_acidente, "Relacionado"])
        print(f"Tabelas para Gephi criadas: {arquivo_arestas} e {arquivo_nos}.")
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}") 

criar_tabelas_gephi(
    "acidentes2024_ano_veiculos_nivel_emergencia.csv", 
    "gephi_arestas.csv", 
    "gephi_nos.csv"
)
