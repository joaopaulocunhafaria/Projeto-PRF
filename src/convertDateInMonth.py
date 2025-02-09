import csv
from datetime import datetime, timedelta

def converDateInMonth(arquivo_entrada, arquivo_saida):
    # Lista de feriados nacionais no Brasil (ano fixo para simplificação)
    feriados = {
        "01-01": "Confraternização Universal",
        "21-04": "Tiradentes",
        "01-05": "Dia do Trabalhador",
        "07-09": "Independência do Brasil",
        "12-10": "Nossa Senhora Aparecida",
        "02-11": "Finados",
        "15-11": "Proclamação da República",
        "25-12": "Natal"
    }

    def verificar_proximidade(data_invertida):
        try:
            data = datetime.strptime(data_invertida, "%Y-%m-%d")
            for feriado, nome in feriados.items():
                mes, dia = map(int, feriado.split('-'))
                data_feriado = datetime(data.year, mes, dia)
                if abs((data - data_feriado).days) <= 2:  # Verifica proximidade de 2 dias
                    return nome
            return ""  # Não está próximo de um feriado
        except ValueError:
            return ""  # Data inválida

    def calcular_semana(data):
        primeiro_dia_mes = data.replace(day=1)
        return ((data - primeiro_dia_mes).days // 7) + 1

    try:
        # Abrindo o arquivo de entrada
        with open(arquivo_entrada, mode='r', encoding='utf-8') as entrada:
            leitor = csv.reader(entrada, delimiter=';')
            
            # Abrindo o arquivo de saída
            with open(arquivo_saida, mode='w', encoding='utf-8', newline='') as saida:
                escritor = csv.writer(saida, delimiter=';')

                # Escrevendo cabeçalho no arquivo de saída
                cabecalho = next(leitor, None)  # Pega a primeira linha como cabeçalho
                if cabecalho:
                    escritor.writerow(cabecalho + ["mes", "semana", "feriado"])

                # Dicionário para contar acidentes por mês e semana
                contador_mes_semana = {}

                # Iterando pelas linhas do arquivo de entrada
                for linha in leitor:
                    if len(linha) >= 3:  # Certificando que há pelo menos 3 colunas
                        data_invertida = linha[2]  # Terceira posição

                        # Verificando o mês, semana e a proximidade com feriados
                        try:
                            data = datetime.strptime(data_invertida, "%Y-%m-%d")
                            mes = data.month
                            semana = calcular_semana(data)
                            nome_feriado = verificar_proximidade(data_invertida)
                            linha.append(mes)  # Adicionando o mês como nova coluna
                            linha.append(semana)  # Adicionando a semana como nova coluna
                            linha.append(nome_feriado)  # Adicionando o nome do feriado ou vazio
                            escritor.writerow(linha)  # Escrevendo a linha no arquivo de saída

                            # Incrementando o contador de acidentes por mês e semana
                            chave = (mes, semana)
                            if chave not in contador_mes_semana:
                                contador_mes_semana[chave] = 0
                            contador_mes_semana[chave] += 1
                        except ValueError:
                            print(f"Formato de data inválido na linha: {linha}")

                # Escrevendo o resumo no final do arquivo
                escritor.writerow([])  # Linha em branco
                escritor.writerow(["Resumo por Mês e Semana:"])
                for (mes, semana), qntd in sorted(contador_mes_semana.items()):
                    escritor.writerow([f"Mês {mes}, Semana {semana}", f"Quantidade de Acidentes: {qntd}"])

        print(f"Linhas filtradas foram salvas em {arquivo_saida}.")

    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
converDateInMonth("acidentes2024_todas_causas_tipos.csv", "acidentes2024_por_mes.csv")
