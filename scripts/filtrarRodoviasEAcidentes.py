import csv
from collections import defaultdict

# Função para processar o arquivo CSV
def processar_acidentes(arquivo_entrada, arquivo_saida):
    # Dicionário para armazenar os dados
    rodovias = defaultdict(lambda: {'Total': 0, 'Graves': 0, 'Feridos': 0, 'Leves': 0})

    # Abrindo o arquivo CSV
    with open(arquivo_entrada, mode='r', encoding='ISO-8859-1') as csvfile:
        leitor = csv.reader(csvfile, delimiter=';')
        next(leitor)  # Pula o cabeçalho
        
        # Iterando por cada linha
        for linha in leitor:
            try:
                uf = linha[5].strip()  # Coluna UF (6ª coluna no índice zero-based)
                rodovia = linha[6].strip()  # Coluna Rodovia (7ª coluna no índice zero-based)
                classificacao = linha[13].strip()  # Classificação do acidente (14ª coluna no índice zero-based)

                if rodovia:  # Verifica se a rodovia está especificada
                    chave_rodovia = f"{uf} {rodovia}"  # Exemplo: "MG 050"
                    rodovias[chave_rodovia]['Total'] += 1

                    # Classificando o tipo de acidente
                    
                    if classificacao == 'Com VÃ­timas Fatais':
                        rodovias[chave_rodovia]['Graves'] += 1
                    elif classificacao == 'Com VÃ­timas Feridas':
                        rodovias[chave_rodovia]['Feridos'] += 1
                    elif classificacao == 'Sem VÃ­timas':
                        rodovias[chave_rodovia]['Leves'] += 1
            except IndexError:
                # Linha inválida, ignorar
                continue

    # Salvando os dados processados em um novo arquivo CSV
    with open(arquivo_saida, mode='w', encoding='utf-8', newline='') as csvfile:
        escritor = csv.writer(csvfile)
        
        # Cabeçalho do arquivo de saída
        escritor.writerow(['Rodovia', 'Acidentes', 'Graves', 'Feridos', 'Leves'])

        # Escrevendo os dados
        for rodovia, dados in rodovias.items():
            escritor.writerow([rodovia, dados['Total'], dados['Graves'], dados['Feridos'], dados['Leves']])

# Executando a função com arquivos de exemplo
arquivo_entrada = 'acidentes2024_todas_causas_tipos.csv'  # Substitua pelo caminho do seu arquivo de entrada
arquivo_saida = 'rodoviasAcidentes.csv'  # Substitua pelo caminho do seu arquivo de saída

processar_acidentes(arquivo_entrada, arquivo_saida)
