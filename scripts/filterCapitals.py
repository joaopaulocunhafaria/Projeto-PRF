import csv

def filtrar_acidentes_capitais(arquivo_entrada, arquivo_saida):
    # Lista das capitais do Brasil sem acentos em maiúsculas
    capitais = [
        "RIO BRANCO", "MACEIO", "MACAPA", "MANAUS", "SALVADOR", "FORTALEZA", "BRASILIA",
        "VITORIA", "GOIANIA", "SAO LUIS", "CUIABA", "CAMPO GRANDE", "BELO HORIZONTE",
        "BELEM", "JOAO PESSOA", "CURITIBA", "RECIFE", "TERESINA", "RIO DE JANEIRO",
        "NATAL", "PORTO ALEGRE", "PORTO VELHO", "BOA VISTA", "FLORIANOPOLIS", "SAO PAULO",
        "ARACAJU", "PALMAS"
    ]

    try:
        # Abrindo o arquivo de entrada
        with open(arquivo_entrada, mode='r', encoding='utf-8') as entrada:
            leitor = csv.reader(entrada, delimiter=';')
            # Abrindo o arquivo de saída
            with open(arquivo_saida, mode='w', encoding='utf-8', newline='') as saida:
                escritor = csv.writer(saida, delimiter=';')

                # Iterando pelas linhas do arquivo de entrada
                for linha in leitor:
                    # Verificando se a nona coluna contém o nome de uma capital
                    if len(linha) >= 9 and linha[8].strip().upper() in capitais:
                        escritor.writerow(linha)

        print(f"Linhas filtradas foram salvas em {arquivo_saida}.")

    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
filtrar_acidentes_capitais("acidentes2024_todas_causas_tipos.csv", "acidentes2024_capitais.csv")
