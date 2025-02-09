import csv
import heapq

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

def ler_matriz_csv(nome_arquivo):
    matriz = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor, None)

        for linha in leitor:
            matriz.append([float(valor) if valor.replace('.', '', 1).isdigit() else float('inf') for valor in linha[1:]])
        
    return matriz

def retorna_rodovia(nome_arquivo, caminho):
    caminhoString = []
    
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        linhas = list(leitor)
        linhas = linhas[1:]

        for indice in caminho:
            if 0 <= indice < len(linhas):
                caminhoString.append(linhas[indice][0])
            else:
                print(f"Aviso: Índice {indice} fora dos limites do arquivo CSV.")

    return caminhoString

def dijkstra(matriz_adj, origem, destino):
    num_nos = len(matriz_adj)
    distancias = [float('inf')] * num_nos
    predecessores = [-1] * num_nos
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        peso_atual, no_atual = heapq.heappop(fila_prioridade)

        if no_atual == destino:
            break

        for vizinho in range(num_nos):
            peso_aresta = matriz_adj[no_atual][vizinho]
            
            if peso_aresta > 0 and peso_atual + peso_aresta < distancias[vizinho]:
                distancias[vizinho] = peso_atual + peso_aresta
                predecessores[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancias[vizinho], vizinho))
    
    caminho = []
    atual = destino
    while atual != -1:
        caminho.append(atual)
        atual = predecessores[atual]
    
    caminho.reverse()

    if distancias[destino] == float('inf'):
        return -1, []

    return distancias[destino], caminho

arquivo_matriz = "graphs/grafo_ligacoes_sem_coeficiente.csv"
matriz_adj = ler_matriz_csv(arquivo_matriz)

#Colocar origem e destino como mapeado na base de dados grafo_ligacoes_sem_coeficiente.csv no diretorio /graphs
origem = "TO 153"
destino = "PR 476"

origem, destino = encontrar_indices(arquivo_matriz, origem, destino)
distancia_minima, caminho_percorrido = dijkstra(matriz_adj, origem, destino)

if distancia_minima == -1:
    print(f"Não há caminho entre {origem} e {destino}.")
else:
    caminho_percorrido = retorna_rodovia(arquivo_matriz, caminho_percorrido)
    print(f"Menor peso do caminho de {retorna_rodovia(arquivo_matriz, [origem])} para {retorna_rodovia(arquivo_matriz, [destino])}: {distancia_minima}")
    print(f"Caminho percorrido: {' -> '.join(map(str, caminho_percorrido))}")
