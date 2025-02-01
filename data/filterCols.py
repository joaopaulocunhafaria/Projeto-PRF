import csv

def extract_columns(arquivo_entrada, arquivo_saida, colunas):
    try:
        # Abrindo o arquivo de entrada
        with open(arquivo_entrada, mode='r', encoding='utf-8') as entrada:
            leitor = csv.reader(entrada, delimiter=';')

            # Abrindo o arquivo de saída
            with open(arquivo_saida, mode='w', encoding='utf-8', newline='') as saida:
                escritor = csv.writer(saida, delimiter=';')

                # Extraindo cabeçalho
                cabecalho = next(leitor, None)  
                if cabecalho:
                    cabecalho_filtrado = [cabecalho[i] for i in colunas]
                    escritor.writerow(cabecalho_filtrado)

                # Iterando pelas linhas e filtrando as colunas desejadas
                for linha in leitor:
                    if len(linha) > max(colunas):
                        linha_filtrada = [linha[i] for i in colunas]
                        escritor.writerow(linha_filtrada)

        print(f"Arquivo com colunas filtradas salvo em {arquivo_saida}.")

    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
# Extraindo as colunas 5, 8, 7, 3 (índices baseados em zero: 4, 7, 6, 2)
extract_columns("acidentes2024_ano_veiculos.csv", "acidentes2024_ano_veiculos_nivel_emergencia.csv", [0,2,7,6])
