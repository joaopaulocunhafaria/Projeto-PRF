import csv
import requests

# Função para obter coordenadas usando uma API
def obter_coordenadas(nome_rodovia, api_key):
    url = "https://api.opencagedata.com/geocode/v1/json"
    nome_rodovia = "Brasil " + nome_rodovia
    params = {
        'q': nome_rodovia,
        'key': api_key,
        'limit': 1
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        dados = response.json()
        if dados['results']:
            latitude = dados['results'][0]['geometry']['lat']
            longitude = dados['results'][0]['geometry']['lng']
            print(f"Coordenadas encontradas para {nome_rodovia}: {latitude}, {longitude}")
            return latitude, longitude
        else:
            print(f"Coordenadas não encontradas para: {nome_rodovia}")
            return None, None
    except Exception as e:
        print(f"Erro ao obter coordenadas para {nome_rodovia}: {e}")
        return None, None

# Função para atualizar o arquivo CSV com as coordenadas
def adicionar_coordenadas_csv(arquivo_entrada, api_key):
    # Lê o arquivo original e carrega o conteúdo na memória
    with open(arquivo_entrada, mode='r', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        cabecalho = next(leitor)  # Lê o cabeçalho
        if "Latitude" not in cabecalho and "Longitude" not in cabecalho:
            cabecalho.extend(["Latitude", "Longitude"])  # Adiciona as novas colunas
        linhas_completas = [cabecalho]

        for linha in leitor:
            nome_rodovia = linha[1]  # Supondo que o nome da rodovia está na coluna "Label"
            latitude, longitude = obter_coordenadas(nome_rodovia, api_key)
            linha.extend([latitude, longitude])  # Adiciona as coordenadas
            linhas_completas.append(linha)

    # Sobrescreve o arquivo original com os dados atualizados
    with open(arquivo_entrada, mode='w', encoding='utf-8', newline='') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerows(linhas_completas)

    print(f"Arquivo {arquivo_entrada} atualizado com sucesso!")

 
arquivo_entrada = 'gephi_nos_rodovias_ligacoes.csv'  # Substitua pelo caminho do seu arquivo CSV
api_key = 'ab3ac22f94ee4b5e88dd63c04922f695'  # Substitua pela sua chave da API

adicionar_coordenadas_csv(arquivo_entrada, api_key)
