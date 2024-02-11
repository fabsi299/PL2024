# PL2024

# TPC1: Análise de um dataset

Autor: Fábio Daniel Rodrigues Leite (a100902)

## Parse CSV

- A função ler_dataset é responsável pela leitura do arquivo CSV.
- Primeiro, ela abre o arquivo especificado pelo caminho_arquivo em modo de leitura.
- Em seguida, ela lê a primeira linha do arquivo para obter os cabeçalhos das colunas. As linhas restantes do arquivo são então lidas e cada linha é dividida em uma lista de valores usando a vírgula como delimitador. 
- Cada linha é transformada em um dicionário onde as chaves são os cabeçalhos das colunas e os valores correspondentes são os valores das células naquela linha. Esses dicionários são agregados em uma lista que é retornada como resultado da função. 

## Lista ordenada alfabeticamente das modalidades desportivas

- Na função ordenar_modalidade começamos por recolher a informação dos dados cujo cabeçalho corresponde a modalidade.
- Após isso criamos um set(uma vez que não permite valores repetidos) e preenchemos o set com todas as modalides presentes.
- Depois utilizamos a função sorted(), ordenando assim o set por ordem alfabetica.

## Percentagens de atletas aptos e inaptos para a prática desportiva

- A função calcular_percentagens começa por determinar o número total de atletas na lista de dados. 
- Após isso, ela itera verifica nos dados se o resultado está marcado como 'true', indicando que o atleta está apto. Com isso, calcula o total de atletas aptos e, consequentemente, o número de atletas inaptos. 
- Utilizando esses números, ela calcula as percentagens de atletas aptos e inaptos em relação ao total de atletas. Caso não haja atletas na lista, as percentagens retornadas são ambas 0.

## Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos)

- A função distribuicao_etaria começa por definir faixas etárias de cinco anos, cobrindo idades até 60 anos. 
- Em seguida, inicializa um dicionário para armazenar a distribuição, onde cada chave representa uma faixa etária e o valor associado é o número de atletas dentro dessa faixa. 
- Iterando sobre as faixas etárias, ela conta quantos atletas possuem idades dentro de cada faixa e armazena essas contagens no dicionário. 
- Por fim , retorna o dicionário contendo a distribuição etária dos atletas, sendo no final apenas apresentadas as faixas etárias que apresentem pelo menos um atleta.



