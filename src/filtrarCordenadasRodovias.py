import csv

def extrair_coordenadas(arquivo_entrada, arquivo_saida):
    rodovias_vistas = set()

    try:
        with open(arquivo_entrada, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')  # Delimitador ajustado para ","
            header = next(reader, None)  # Lê o cabeçalho e evita erro se estiver vazio
            
            if not header:
                print("Erro: O arquivo de entrada está vazio ou sem cabeçalho.")
                return

            # Criando o arquivo de saída
            with open(arquivo_saida, mode='w', encoding='utf-8', newline='') as output_file:
                writer = csv.writer(output_file, delimiter=',')  # Garantindo compatibilidade com Gephi
                writer.writerow(["Rodovia", "Latitude", "Longitude"])  # Cabeçalho

                # Processando cada linha do arquivo de entrada
                for linha in reader:
                    try:
                        estado = linha[5].strip()
                        numero_br = linha[6].strip()
                        latitude = linha[32].strip()
                        print("Latitude: ", latitude)
                        longitude = linha[33].strip()
                        print("Longitude: ", longitude)
                        rodovia = f"{estado} {numero_br}"

                        # Evita duplicatas no arquivo final
                        if rodovia not in rodovias_vistas:
                            writer.writerow([rodovia, latitude, longitude])
                            rodovias_vistas.add(rodovia)

                    except IndexError:
                        print(f"Erro ao processar linha (colunas ausentes): {linha}")

        print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Configuração inicial
arquivo_entrada = "acidentes2024_todas_causas_tipos.csv"
arquivo_saida = "coordenadasRodovias.csv"

# Executando a função
extrair_coordenadas(arquivo_entrada, arquivo_saida)
