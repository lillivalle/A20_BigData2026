#Atividade 02

# Estudo mais detalhado de como os dados estão distribuidos ao longo do tempo
# Identificar maiores e menores qtnd de estelionatos, expor meses/ano que 
# apresentam quantidades muito acima do comportamento dos demais períodos analisados

import pandas as pd 
import numpy as np 
# pip install matplotlib
import matplotlib.pyplot as plt

try:
    print('Obtendo os dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# utf-8,iso-8859-1, latin1, cp1252
    df_dadoscompletos = pd.read_csv(ENDERECO_DADOS, sep =';' , encoding='iso-8859-1')
#    print(df_dadoscompletos)

# pegando as variáveis
    df_estelionato_ano = df_dadoscompletos[['mes_ano','estelionato']]
    df_estelionato_ano = df_estelionato_ano.groupby('mes_ano', as_index=False)[['estelionato']].sum()
    df_estelionato_ano = df_estelionato_ano.sort_values(by='estelionato', ascending=True)


    # iqr (Intervalo Interquartil) - Amplitude dos 50% dados mais centrais.
    # iqr = q3 - q1 
    # Ele ignora os valores extremos. Max e Min estão fora do Interquartil (IQR)
    # Não sofre interferência dos valores extremos (outliers)
    # Quanto mais próximo do q1 (ou zero), mais homogêneos são os dados
    # Quanto mais próximo de q3, menos homogêneos são os dados

    array_estelionato = np.array(df_estelionato_ano['estelionato'])
    media_estelionato = np.mean(array_estelionato)
    
    q1 = np.quantile(array_estelionato, .25)
    mediana_estelionato = np.median(array_estelionato)
    q3 = np.quantile(array_estelionato, .75)

    distancia = abs((media_estelionato - mediana_estelionato) / mediana_estelionato * 100)
    array_estelionato = np.array(df_estelionato_ano['estelionato'])
    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)

    iqr = q3 - q1

    #Limite inferior
    #Identificando outliers, os valores abaixo dele
    limite_inferior = q1 - (1.5 * iqr)

    #Limite superior
    #Identificando outliers, os valores acima dele
    limite_superior = q3 + (1.5 * iqr)

    print('\nMedidas ')
    print(30*'=')
#    print(f'Mínimo: {minimo}')
    print(f'Limite Inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Mediana: {mediana_estelionato}') #q2
    print(f'Q3: {q3}')
    print(f'Limite Superior: {limite_superior}')
#    print(f'Máximo: {maximo}')
    
    #outliers superiores
    df_estelionato_ano_outliers_superiores = df_estelionato_ano[df_estelionato_ano['estelionato'] > limite_superior] 
    #outliers inferiores
    df_estelionato_ano_outliers_inferiores = df_estelionato_ano[df_estelionato_ano['estelionato'] < limite_inferior] 

    print('\nEstelionatos c/ Outliers Inferiores ')
    print(30*"=")
    if len(df_estelionato_ano_outliers_inferiores) == 0:
        print('Não existe outliers inferiores')
    else:
        print(df_estelionato_ano_outliers_inferiores.sort_values(by='estelionato', ascending=True))


    print('\nMunicípios c/ Outliers Superiores ')
    print(30*"=")
    if len(df_estelionato_ano_outliers_superiores) == 0:
        print('Não existe outliers superiores')
    else:
        print(df_estelionato_ano_outliers_superiores.sort_values(by='estelionato', ascending=False))

except Exception as e:
    print(f'Erro ao calcular {e}')

try:
        plt.figure(figsize=(18, 8))
        plt.subplots(2, 1)

        plt.subplot(2,1,1) # subplot de duas linhas e uma coluna na posição 1
        plt.boxplot(array_estelionato, vert=False, showmeans=True)

        plt.subplot(2,1,2) #subplor de duas linhas e uma coluna na posição 2
        plt.text(0.1, 0.9, f'Média: {media_estelionato:.2f}')
        plt.text(0.1, 0.8, f'Mediana: {mediana_estelionato:.2f}')
        plt.text(0.1, 0.7, f'Distância: {distancia:.2f}')
        plt.text(0.1, 0.6, f'Mínimo: {minimo:.2f}')
        plt.text(0.1, 0.5, f'Máximo: {maximo:.2f}')
        plt.show()

except Exception as e:
    print(f'Erro ao calcular {e}')