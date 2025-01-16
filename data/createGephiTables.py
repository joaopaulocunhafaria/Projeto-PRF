import csv

def criar_tabelas_gephi(arquivo_entrada, arquivo_arestas, arquivo_nos):
    try:
        # Abrindo o arquivo de entrada
        with open(arquivo_entrada, mode='r', encoding='utf-8') as entrada:
            leitor = csv.reader(entrada, delimiter=';')
            
            # Lendo o cabeçalho
            cabecalho = next(leitor, None)
            if not cabecalho:
                print("Erro: O arquivo de entrada está vazio ou não possui cabeçalho.")
                return

            # Índices das colunas relevantes
            indices = {
                "id": cabecalho.index("id"),
                "classificacao_acidente": cabecalho.index("classificacao_acidente"),
                "ano_fabricacao_veiculo": cabecalho.index("ano_fabricacao_veiculo"),
                "marca": cabecalho.index("marca"),
            }

            # Abrindo arquivos de saída
            with open(arquivo_arestas, mode='w', encoding='utf-8', newline='') as saida_arestas:
                with open(arquivo_nos, mode='w', encoding='utf-8', newline='') as saida_nos:

                    escritor_arestas = csv.writer(saida_arestas, delimiter=';')
                    escritor_nos = csv.writer(saida_nos, delimiter=';')

                    # Escrevendo cabeçalhos
                    escritor_arestas.writerow(["Source", "Target", "Relationship"])
                    escritor_nos.writerow(["Id", "Label", "Category"])

                    # Conjuntos para evitar duplicatas de nós
                    nos = set()

                    # Processando linhas do arquivo de entrada
                    for linha in leitor:
                        id_acidente = linha[indices["id"]]
                        classificacao_acidente = linha[indices["classificacao_acidente"]]
                        ano_fabricacao_veiculo = linha[indices["ano_fabricacao_veiculo"]]
                        marca = linha[indices["marca"]]

                        # Criando nó do ano de fabricação (central)
                        if ano_fabricacao_veiculo not in nos:
                            escritor_nos.writerow([ano_fabricacao_veiculo, ano_fabricacao_veiculo, "Ano de Fabricação"])
                            nos.add(ano_fabricacao_veiculo)

                        # Criando nó da marca do veículo
                        if marca not in nos:
                            escritor_nos.writerow([marca, "", "Marca"])
                            nos.add(marca)

                        # Criando nó da classificação do acidente
                            escritor_nos.writerow([classificacao_acidente, "", "Classificação do Acidente"])
                        if classificacao_acidente not in nos:
                            nos.add(classificacao_acidente)

                        # Criando arestas entre o ano de fabricação e os outros nós
                        escritor_arestas.writerow([ano_fabricacao_veiculo,classificacao_acidente, "Relacionado"])
                        # escritor_arestas.writerow([ano_fabricacao_veiculo, "", "Relacionado"])

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
