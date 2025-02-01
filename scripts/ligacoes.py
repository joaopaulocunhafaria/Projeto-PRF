import csv


rodovias_conexoes = {
    "RJ 101": ["ES 101", "RJ 116"],
    "GO 153": ["TO 153", "SP 153"],
    "ES 101": ["RJ 101", "BA 101"],
    "SC 101": ["RS 101", "PR 101"],
    "RS 116": ["RJ 116", "SC 116"],
    "PR 277": ["PR 116", "MS 267"],
    "RS 158": ["MS 158", "PR 158"],
    "MS 262": ["MS 267", "SP 262"],
    "RO 364": ["AC 364", "MT 364"],
    "SP 101": ["SP 116", "MG 101"],
    "PR 376": ["PR 277", "SC 376"],
    "PR 369": ["PR 376", "SP 369"],
    "ES 262": ["MG 262", "RJ 262"],
    "GO 60": ["DF 60", "GO 70"],
    "MG 381": ["SP 381", "ES 381"],
    "DF 60": ["GO 60", "DF 40"],
    "PR 153": ["SC 153", "MG 153"],
    "GO 80": ["GO 70", "DF 80"],
    "PI 316": ["PI 343", "MA 316"],
    "PI 343": ["PI 316", "CE 343"],
    "RS 386": ["RS 285", "RS 290"],
    "BA 116": ["BA 101", "MG 116"],
    "PE 428": ["PE 407", "PE 232"],
    "SC 280": ["SC 470", "PR 280"],
    "PE 101": ["SE 101", "PB 101"],
    "SE 235": ["BA 235", "SE 101"],
    "PR 116": ["RS 116", "SP 116"],
    "SE 101": ["PE 101", "BA 101"],
    "MS 60": ["GO 60", "MS 267"],
    "DF 20": ["GO 20", "DF 40"],
    "MG 365": ["MG 262", "GO 365"],
    "RJ 356": ["MG 356", "RJ 116"],
    "PR 373": ["PR 277", "PR 466"],
    "MG 262": ["ES 262", "MG 381"],
    "PB 101": ["PE 101", "PB 230"],
    "MG 40": ["RJ 40", "DF 40"],
    "TO 153": ["GO 153", "PA 153"],
    "SC 116": ["RS 116", "PR 116"],
    "MT 364": ["RO 364", "GO 364"],
    "CE 304": ["RN 304", "PI 304"],
    "PB 230": ["PE 230", "PI 230"],
    "PE 110": ["PB 110", "AL 110"],
    "MG 251": ["GO 251", "DF 251"],
    "AL 316": ["PE 316", "SE 316"],
    "SP 116": ["RJ 116", "PR 116"],
    "SC 282": ["SC 470", "SC 163"],
    "MT 163": ["MS 163", "PA 163"],
    "ES 393": ["RJ 393", "MG 393"],
    "RS 101": ["SC 101", "RS 116"],
    "RN 101": ["RN 304", "RN 406"],
    "RN 406": ["RN 101", "CE 406"],
    "RJ 116": ["SP 116", "RS 116"],
    "RS 392": ["RS 285", "RS 290"],
    "RS 285": ["RS 386", "RS 392"],
    "BA 324": ["BA 101", "BA 242"],
    "CE 116": ["RN 116", "PI 116"],
    "RS 290": ["RS 386", "RS 392"],
    "AL 101": ["PE 101", "SE 101"],
    "GO 70": ["DF 70", "GO 60"],
    "BA 101": ["ES 101", "SE 101"],
    "GO 364": ["MT 364", "GO 60"],
    "GO 50": ["GO 60", "GO 40"],
    "SP 381": ["MG 381", "ES 381"],
    "PI 222": ["PI 135", "MA 222"],
    "RJ 40": ["MG 40", "DF 40"],
    "SC 470": ["SC 282", "SC 480"],
    "SC 480": ["SC 470", "SC 285"],
    "PA 316": ["PA 163", "PI 316"],
    "PR 163": ["SC 163", "MS 163"],
    "MS 163": ["MT 163", "PR 163"],
    "MG 116": ["RJ 116", "BA 116"],
    "MG 267": ["SP 267", "RJ 267"],
    "RN 304": ["CE 304", "RN 101"],
    "PA 10": ["PA 230", "TO 10"],
    "AC 364": ["RO 364", "AC 317"],
    "MS 158": ["RS 158", "GO 158"],
    "MG 146": ["MG 354", "SP 146"],
    "BA 242": ["BA 324", "TO 242"],
    "MA 135": ["PI 135", "MA 222"],
    "PE 408": ["PE 110", "PE 232"],
    "MS NA": [],
    "AL 104": ["PE 104", "AL 110"],
    "GO 452": ["GO 50", "GO 158"],
    "SC 163": ["MS 163", "SC 282"],
    "PE 104": ["PB 104", "AL 104"],
    "RJ NA": [],
    "RS 470": ["SC 470", "RS 480"],
    "PR 158": ["RS 158", "SC 158"],
    "PE 232": ["PE 408", "PE 428"],
    "PE 423": ["PE 407", "AL 423"],
    "DF 70": ["GO 70", "DF 60"],
    "PR 476": ["PR 272", "PR 487"],
    "GO 40": ["RJ 40", "GO 50"],
    "MT 174": ["RO 174", "MT 70"],
    "MT 70": ["GO 70", "MT 174"],
    "MA 230": ["PI 230", "CE 230"],
    "RJ 493": ["RJ 116", "RJ 393"],
    "CE 222": ["PI 222", "MA 222"],
    "MG 153": ["GO 153", "PR 153"],
    "PE 316": ["AL 316", "PE 408"],
    "RS 287": ["RS 290", "RS 386"],
    "MG 50": ["GO 50", "DF 50"],
    "RN 110": ["PB 110", "RN 304"],
    "PI 135": ["MA 135", "PI 222"],
    "GO 158": ["MS 158", "GO 452"],
    "GO 20": ["DF 20", "BA 20"],
    "BA 110": ["SE 110", "PE 110"],
    "MA 222": ["PI 222", "MA 135"],
    "MA 10": ["PA 10", "MA 226"],
    "SP 153": ["GO 153", "TO 153"],
    "RJ 393": ["ES 393", "RJ 493"],
    "RS NA": [],
    "MT 158": ["GO 158", "RS 158"],
    "PI 235": ["MA 235", "TO 235"],
    "PB 104": ["PE 104", "PB 110"],
    "MG 354": ["MG 146", "SP 354"],
    "TO 10": ["PA 10", "TO 226"],
    "DF 80": ["GO 80", "DF 40"],
    "RS 468": ["RS 472", "RS 480"],
    "MA 226": ["MA 10", "PI 226"],
    "RN 427": ["RN 110", "PB 427"],
    "RJ 465": ["RJ 40", "RJ 493"],
    "BA 20": ["GO 20", "DF 20"],
    "RS 293": ["RS 287", "RS 290"],
    "PA 230": ["PI 230", "AM 230"],
    "CE 20": ["RN 20", "PI 20"],
    "BA 418": ["BA 101", "MG 418"],
    "RN 405": ["RN 101", "PB 405"],
    "SC 153": ["PR 153", "SC 282"],
    "PE 424": ["AL 424", "PE 423"],
    "RS 448": ["RS 386", "RS 290"],
    "PA 163": ["MT 163", "PA 316"],
    "RN 226": ["CE 226", "PI 226"],
    "GO 251": ["MG 251", "DF 251"],
    "RO 319": ["AM 319", "AC 319"],
    "RS 153": ["PR 153", "SC 153"],
    "GO 414": ["DF 414", "GO 60"],
    "BA 235": ["SE 235", "MA 235"],
    "CE 230": ["MA 230", "PI 230"],
    "TO 235": ["MA 235", "PI 235"],
    "PE 407": ["PE 428", "PE 423"],
    "RS 472": ["RS 468", "RS 293"],
    "MA 316": ["PI 316", "MA 10"],
    "BA 415": ["BA 101", "MG 415"],
    "MS 463": ["MS 267", "PY 463"],
    "DF 251": ["MG 251", "GO 251"],
    "PB 116": ["PE 116", "RN 116"],
    "RR 401": ["RR 432", "RR 174"],
    "PA 222": ["MA 222", "PI 222"],
    "PI 230": ["MA 230", "PA 230"],
    "MS 267": ["MS 262", "PR 267"],
    "AP 210": ["AP 156", "AP 317"],
    "SP 459": ["MG 459", "SP 354"],
    "TO 230": ["MA 230", "PI 230"],
    "DF 40": ["RJ 40", "DF 20"],
    "BA 407": ["BA 116", "PE 407"],
    "BA 349": ["SE 349", "GO 349"],
    "RO 435": ["RO 364", "MT 435"],
    "RO 429": ["RO 319", "RO 364"],
    "AL 423": ["PE 423", "AL 110"],
    "PB 405": ["RN 405", "PB 230"],
    "ES 259": ["MG 259", "ES 262"],
    "PA 155": ["TO 155", "PA 163"],
    "BA 330": ["MA 330", "MG 330"],
    "MG 459": ["SP 459", "RJ 459"],
    "PB 361": ["PB 230", "PE 361"],
    "SP 488": ["SP 101", "SP 459"],
    "AM 319": ["RO 319", "RR 319"],
    "MA 402": ["PI 402", "CE 402"],
    "MS 436": ["MS 267", "PR 436"],
    "PE 116": ["PB 116", "RN 116"],
    "BA 410": ["BA 101", "BA 242"],
    "AC 317": ["RO 364", "AM 317"],
    "RR 432": ["RR 401", "RR 319"],
    "PR 467": ["PR 163", "SC 467"],
    "RR 174": ["AM 174", "RR 401"],
    "MS 376": ["PR 376", "MS 267"],
    "PR 469": ["SC 469", "PR 467"],
    "AP 156": ["AP 210", "AP 317"],
    "RS 471": ["RS 472", "RS 448"],
    "PA 308": ["PA 316", "PA 155"],
    "MG 364": ["GO 364", "RJ 364"],
    "PB 427": ["RN 427", "PB 230"],
    "BA 135": ["PI 135", "MA 135"],
    "MG 356": ["RJ 356", "MG 262"],
    "BA 367": ["MG 367", "BA 101"],
    "TO 242": ["BA 242", "TO 153"],
    "SC 158": ["PR 158", "RS 158"],
    "RO 174": ["MT 174", "RO 364"],
    "AM 174": ["RR 174", "AM 317"],
    "BA 420": ["BA 324", "BA 242"],
    "TO NA": [],
    "AL NA": [],
    "RJ 354": ["MG 354", "RJ 116"],
    "PR 272": ["PR 476", "PR 373"],
    "ES 447": ["RJ 447", "MG 447"],
    "AM 230": ["PA 230", "RR 230"],
    "PI 407": ["PE 407", "MA 407"],
    "SC NA": [],
    "SE 349": ["BA 349", "SE 101"],
    "RO NA": [],
    "CE 122": ["RN 122", "PI 122"],
    "PB 110": ["PE 110", "RN 110"],
    "RJ 495": ["RJ 116", "RJ 101"],
    "PI 20": ["CE 20", "RN 20"],
    "RO 421": ["RO 429", "RO 364"],
    "PE NA": [],
    "MS 359": ["MS 267", "GO 359"]
    }


import csv

def gerar_dados_gephi(arquivo_entrada, arquivo_nos, arquivo_arestas):
    # Inicializa contadores de IDs
    id_counter = 1
    rodovia_ids = {}
    
    # Listas para armazenar nós e arestas
    nos = []
    arestas = []

    # Lendo o arquivo CSV de entrada
    try:
        with open(arquivo_entrada, mode='r', encoding='utf-8') as csvfile:
            leitor = csv.reader(csvfile, delimiter=',')
            cabecalho = next(leitor, None)  # Lê o cabeçalho
            linhas = list(leitor)  # Carrega todas as linhas na memória

            # Iterando pelas linhas do arquivo
            for linha in linhas:
                print(linha)  # Para debug
                rodovia = linha[0]  # Nome da rodovia
                total = int(linha[1])  # Total de acidentes

                # Verifica se a rodovia já tem um ID atribuído
                if rodovia not in rodovia_ids:
                    rodovia_ids[rodovia] = id_counter
                    nos.append([id_counter, rodovia, "Rodovia"])
                    id_counter += 1

                rodovia_id = rodovia_ids[rodovia]

                # Verifica as conexões da rodovia atual
                if rodovia in rodovias_conexoes:
                    for rodovia_conectada in rodovias_conexoes[rodovia]:
                        # Verifica se a rodovia conectada já tem um ID
                        if rodovia_conectada not in rodovia_ids:
                            rodovia_ids[rodovia_conectada] = id_counter
                            nos.append([id_counter, rodovia_conectada, "Rodovia"])
                            id_counter += 1
                        
                        rodovia_conectada_id = rodovia_ids[rodovia_conectada]
                        
                        # Calcular o peso da aresta: média dos acidentes
                        total_conectada = 0
                        for linha_conectada in linhas:  # Reutilizando as linhas carregadas
                            if linha_conectada[0] == rodovia_conectada:
                                total_conectada = int(linha_conectada[1])
                                break
                        peso_aresta = (total + total_conectada) / 2
                        arestas.append([rodovia_id, rodovia_conectada_id, peso_aresta])
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
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
arquivo_nos = 'gephi_nos_rodovias_ligacoes.csv'  # Arquivo de saída para os nós
arquivo_arestas = 'gephi_arestas_rodovias_ligacoes.csv'  # Arquivo de saída para as arestas

gerar_dados_gephi(arquivo_entrada, arquivo_nos, arquivo_arestas)
