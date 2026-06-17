#Atividade 01

#Identificar quais meses e anos (meses_ano) apresentaram maiores e menores
# quantidades de estelionatos, comparando esses períodos com o total de registros
# compreender como os casos estão distribuídos ao longo do tempo 
# se tem padrão nas ocorrências, identificar períodos com menores índices 
# e maior concentração de casos

#tacar o requirements da aula passada e
# pip install -r ./requirements.txt
# que já vai baixar todas as bibliotecas do último exemplo

import pandas as pd 
import numpy as np 
# pip install matplotlib
import matplotlib.pyplot as plt

try:
    print('Obtendo os dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# utf-8,iso-8859-1, latin1, cp1252
    df_dadoscompletos = pd.read_csv(ENDERECO_DADOS, sep =';' , encoding='iso-8859-1')
    print(df_dadoscompletos)

# pegando as variáveis
    df_estelionato_ano = df_dadoscompletos[['mes_ano','estelionato']]

# totalizando os estelionatos por ano
    df_estelionato_ano = df_estelionato_ano.groupby('mes_ano', as_index=False)[['estelionato']].sum()
# as_index -> coloca como 'False' pra não colocar como índice da distribuição    
# .sum()   -> calcular a soma de um conjunto de valores numéricos  
    print(df_estelionato_ano)
#    print(df_estelionato_ano.head())

    print('------------------------------------------------')
    print(' ')
    print('Dados de estelionato em ordem crescente: ')
    print(' ')
# ordenando o dataframe
    df_estelionato_ano = df_estelionato_ano.sort_values(by='estelionato', ascending=True)
# .sort_values  -> organizar e ordenar com base nos valores de uma ou mais colunas em ordem crescente ou decrescente
# em ordem crescente -> ascendig=True    
    print(df_estelionato_ano)

#except Exception as e:
#    print(f'Erro ao obter dados {e}')


# obtendo medidas
    print('Calculando as medidas...')
    array_estelionato = np.array(df_estelionato_ano['estelionato'])

    media_estelionato = np.mean(array_estelionato)
    mediana_estelionato = np.median(array_estelionato)
    distancia = abs((media_estelionato - mediana_estelionato) / mediana_estelionato * 100)

    print('\n ___Medida de Tendência Central___ ')
    print(30*' - ')
    print(f'Média dos estelionatos: {media_estelionato:.2f}')
    print(f'Mediana dos estelionatos: {mediana_estelionato:.2f}')
    print(f'Distância: {distancia:.2f} %')
    print('Se a média e mediana forem muito diferentes não tem um padrão')

#Medida de Distância:
#distancia ate 10% distribuição tem tendencia simetrica / 
# até 25% a tendencia a distribuição apresentam uma certa assimetria - assimetria moderada - certa dispersão.... extremos estão influenciando no resultado
# média deve ser descartada / dados assimetricos')
    
    print(' ')
# Obtendo medidas descritivas
    
#    try:
    print('Processando quartis...')

    q1 = np.quantile(array_estelionato, .25)
    #mediana e q2 é o mesmo
    q3 = np.quantile(array_estelionato, .75)

    print('\nQuartis (Weibull)')
    print(30*' - ')
    print(f'Q1: {q1}')
    print(f'Mediana: {mediana_estelionato}')
    print(f'Q3: {q3}')

#Períodos com menor estelionato
    df_estelionato_ano_menores = df_estelionato_ano[df_estelionato_ano['estelionato'] < q1]

#Períodos com maior estelionato
    df_estelionato_ano_maiores = df_estelionato_ano[df_estelionato_ano['estelionato'] > q3]

    print('\nPeríodo com o menor número de estelionatos: ')
    print(30*'-')
    print(df_estelionato_ano_menores.sort_values(by='estelionato', ascending=True))
        
    print('\nPeríodo com o maior número de estelionatos: ')
    print(df_estelionato_ano_maiores.sort_values(by='estelionato', ascending=True))

# medidas de dispersão
    array_estelionato = np.array(df_estelionato_ano['estelionato'])
    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)
    amplitude = maximo - minimo
    print('\nMedidas de dispersão')
    print(30*'=')
    print(f'Máximo de estelionato: {maximo}')
    print(f'Mínimo de estelionato: {minimo}')

except Exception as e:
    print(f'Erro ao calcular {e}')

