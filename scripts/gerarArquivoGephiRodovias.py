import csv

# Função para gerar arquivos de nós e arestas para o Gephi
def gerar_dados_gephi(arquivo_entrada, arquivo_nos, arquivo_arestas):
    # Inicializa contadores de IDs
    id_counter = 1
    rodovia_ids = {}
    
    # Listas para armazenar nós e arestas
    nos = []
    arestas = []

    # Lendo o arquivo CSV de entrada
    with open(arquivo_entrada, mode='r', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)  # Pula o cabeçalho

        # Iterando pelas linhas do arquivo
        for linha in leitor:
            rodovia = linha[0]  # Nome da rodovia
            total = int(linha[1])  # Total de acidentes
            graves = int(linha[2])  # Acidentes graves
            feridos = int(linha[3])  # Acidentes com feridos
            leves = int(linha[4])  # Acidentes leves

            # Verifica se a rodovia já tem um ID atribuído
            if rodovia not in rodovia_ids:
                rodovia_ids[rodovia] = id_counter
                nos.append([id_counter, rodovia, "Rodovia"])
                id_counter += 1

            rodovia_id = rodovia_ids[rodovia]

            # Adiciona nós para cada característica da rodovia
            caracteristicas = [
                ("Total de Acidentes", total),
                ("Acidentes Graves", graves),
                ("Acidentes com Feridos", feridos),
                ("Acidentes Leves", leves)
            ]

            for nome, valor in caracteristicas:
                if valor > 0:  # Apenas cria nós e arestas se houver valor
                    caracteristica_id = id_counter
                    nos.append([caracteristica_id, f"{nome} ({rodovia})", nome])
                    id_counter += 1

                    # Cria uma aresta ligando a rodovia à característica
                    arestas.append([rodovia_id, caracteristica_id, valor])

    # Escrevendo o arquivo de nós
    with open(arquivo_nos, mode='w', encoding='utf-8', newline='') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(["Id", "Label", "Type"])
        escritor.writerows(nos)

    # Escrevendo o arquivo de arestas
    with open(arquivo_arestas, mode='w', encoding='utf-8', newline='') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(["Source", "Target", "Weight"])
        escritor.writerows(arestas)

# Executando a função com arquivos de exemplo
arquivo_entrada = 'rodoviasAcidentes.csv'  # Arquivo de entrada processado
arquivo_nos = 'gephi_nos.csv'  # Arquivo de saída para os nós
arquivo_arestas = 'gephi_arestas.csv'  # Arquivo de saída para as arestas

gerar_dados_gephi(arquivo_entrada, arquivo_nos, arquivo_arestas)
