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
    print('------------------------------------------------')
    print(' ')
    print('Dados de estelionato em ordem crescente: ')
    print(' ')
# ordenando o dataframe
    df_estelionato_ano = df_estelionato_ano.sort_values(by='estelionato', ascending=True)
# .sort_values  -> organizar e ordenar com base nos valores de uma ou mais colunas em ordem crescente ou decrescente
# em ordem crescente -> ascendig=True    
    print(df_estelionato_ano)

except Exception as e:
    print(f'Erro ao obter dados {e}')


# obtendo medidas
    print('Calculando as medidas...')
    array_estelionato = np.array(df_estelionato_ano['estelionato'])

    media_estelionato = np.mean(array_estelionato)
    mediana_estelionato = np.median(array_estelionato)
    distancia = abs((media_estelionato - mediana_estelionato) / mediana_estelionato * 100)

    print('\n Medida de Tendência Central ')
    print(30*' - ')
    print(f'Média: {media_estelionato}')
    print(f'Mediana: {mediana_estelionato}')
    print(f'Distância: {distancia} %')