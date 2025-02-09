import csv
from collections import deque

def encontrar_indices(nome_arquivo, origem, destino):
    indice_origem = None
    indice_destino = None

    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor, None)

        for indice, linha in enumerate(leitor):
            if linha:
                if linha[0] == origem:
                    indice_origem = indice
                if linha[0] == destino:
                    indice_destino = indice
            if indice_origem is not None and indice_destino is not None:
                break

    return indice_origem, indice_destino

def retorna_rodovia(nome_arquivo, caminho):
    rodovias = []

    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        linhas = list(leitor)[1:]

        for indice in caminho:
            if 0 <= indice < len(linhas):
                rodovias.append(linhas[indice][0])
            else:
                print(f"Aviso: Índice {indice} fora dos limites do arquivo CSV.")

    return rodovias

def ler_matriz_csv(nome_arquivo):
    matriz = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor, None)

        for linha in leitor:
            matriz.append([int(valor) for valor in linha[1:]])

    return matriz

def bfs_menor_caminho(matriz_adj, origem, destino):
    num_nos = len(matriz_adj)
    distancias = [-1] * num_nos
    predecessores = [-1] * num_nos

    distancias[origem] = 0
    fila = deque([origem])

    while fila:
        atual = fila.popleft()

        if atual == destino:
            break

        for vizinho in range(num_nos):
            if matriz_adj[atual][vizinho] > 0 and distancias[vizinho] == -1:
                distancias[vizinho] = distancias[atual] + 1
                predecessores[vizinho] = atual
                fila.append(vizinho)

    if distancias[destino] == -1:
        return -1, []

    caminho = []
    atual = destino
    while atual != -1:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()

    return distancias[destino], caminho

arquivo_matriz = "graphs/grafo_ligacoes_sem_coeficiente.csv"
matriz_adj = ler_matriz_csv(arquivo_matriz)

#Colocar origem e destino como mapeado na base de dados grafo_ligacoes_sem_coeficiente.csv no diretorio /graphs
origem_nome = "TO 153"
destino_nome = "PR 476"
origem, destino = encontrar_indices(arquivo_matriz, origem_nome, destino_nome)

if origem is None or destino is None:
    print("Erro: Rodovia de origem ou destino não encontrada no arquivo.")
else:
    menor_arestas, caminho_percorrido = bfs_menor_caminho(matriz_adj, origem, destino)
    rodovias_caminho = retorna_rodovia(arquivo_matriz, caminho_percorrido)
    print(f"Menor número de arestas de {origem_nome} para {destino_nome}: {menor_arestas}")
    print(f"Caminho percorrido: {' -> '.join(rodovias_caminho)}")
