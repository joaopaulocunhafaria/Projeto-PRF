<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
</head>
<body>

<h1>📌 Análise de Acidentes Rodoviários com Grafos</h1>

<p>Este repositório contém todas as implementações desenvolvidas para a modelagem e análise de acidentes rodoviários utilizando a teoria dos grafos. O projeto inclui a geração e processamento de dados, bem como a aplicação de algoritmos clássicos de grafos para extração de informações relevantes.</p>

<h2>📂 Estrutura do Repositório</h2>

<ul>
    <li><strong>/graphs</strong> - Contém os arquivos CSV gerados representando os grafos utilizados na análise.</li>
    <li><strong>/dataset</strong> - Base de dados utilizada para os experimentos.</li>
    <li><strong>/plots</strong> - Gráficos e imagens geradas ao longo do estudo.</li>
    <li><strong>/src</strong> - Scripts responsáveis pelo processamento dos dados e modelagem dos grafos.</li>
</ul>

<h2>🖥️ Implementações</h2>

<p>Os seguintes scripts foram desenvolvidos e organizados no diretório <strong>/src</strong>:</p>

<ul>
    <li><code>adicionarCordenadas.py</code> - Adiciona coordenadas geográficas às rodovias.</li>
    <li><code>bsf.py</code> - Implementação do algoritmo de Busca em Largura (BFS).</li>
    <li><code>convertDateInMonth.py</code> - Converte datas do dataset para formato mensal.</li>
    <li><code>createGephiTables.py</code> - Gera tabelas de nós e arestas para visualização no Gephi.</li>
    <li><code>criarGrafoGephiAcidentesAcimaMedia.py</code> - Filtra e cria um grafo apenas com rodovias que possuem acidentes acima da média.</li>
    <li><code>dijskstra.py</code> - Implementação do algoritmo de Dijkstra para encontrar caminhos mínimos.</li>
    <li><code>filterCols.py</code> - Filtra colunas específicas do dataset.</li>
    <li><code>filtrarCordenadasRodovias.py</code> - Filtra as rodovias presentes no dataset para mapear coordenadas.</li>
    <li><code>filtrarRodoviaAcidentesAcimaMedia.py</code> - Filtra rodovias com um número elevado de acidentes.</li>
    <li><code>filtrarTotalAcidentes.py</code> - Seleciona rodovias com base no total de acidentes registrados.</li>
    <li><code>gerarMatrizAdjacenciaComCoeficiente.py</code> - Cria a matriz de adjacência ponderada pelo coeficiente de fatalidade.</li>
    <li><code>gerarMatrizAdjacencia.py</code> - Gera a matriz de adjacência das rodovias baseada nas conexões.</li>
    <li><code>ligacoesgephiComCoeficientes.py</code> - Gera as ligações entre rodovias no formato Gephi, ponderadas pelo coeficiente de fatalidade.</li>
    <li><code>ligacoesgephiSemCoeficientes.py</code> - Gera as ligações entre rodovias sem considerar o coeficiente de fatalidade.</li>
    <li><code>mediaAcidentes.py</code> - Calcula a média de acidentes nas rodovias.</li>
    <li><code>plotCordinatesComVitimas.py</code> - Plota gráficos de acidentes considerando vítimas fatais.</li>
    <li><code>plotCordinates.py</code> - Gera visualizações espaciais das rodovias.</li>
    <li><code>totalAcidentes.py</code> - Processa e contabiliza o número total de acidentes por rodovia.</li>
</ul>

<h2>📊 Visualização dos Dados</h2>

<p>Os grafos gerados podem ser visualizados no <a href="https://gephi.org/" target="_blank">Gephi</a>. As tabelas de nós e arestas são compatíveis com o formato do software, permitindo análises mais aprofundadas da estrutura viária e dos padrões de acidentes.</p>

<h2>🛠️ Tecnologias Utilizadas</h2>

<ul>
    <li>Python</li>
    <li>Gephi (para visualização dos grafos)</li>
</ul>

<h2>📌 Como Executar</h2>

<p>Para rodar os scripts, certifique-se de ter o Python instalado e execute:</p>

<pre><code>python3 src/nome_do_script.py</code></pre>

<p>Para visualizar os grafos gerados:</p>

<pre><code>Abra os arquivos CSV do diretório <strong>/graphs</strong> no Gephi</code></pre>

</body>
</html>
