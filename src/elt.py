import pandas as pd

# Carregar dados
selic = pd.read_csv('data/raw/selic_4189.csv', sep=';',
                    decimal=',', encoding='latin1')
credito = pd.read_csv('data/raw/concessoes_pf_20633.csv',
                      sep=';', decimal=',', encoding='latin1')
juros = pd.read_csv('data/raw/taxa_juros_pf_20716.csv',
                    sep=';', decimal=',', encoding='latin1')

# Renomear colunas
selic.rename(columns={
             '4189 - Taxa de juros - Selic acumulada no mês anualizada base 252 - % a.a.': 'Selic'}, inplace=True)
credito.rename(columns={
               '20633 - Concessões de crédito - Pessoas físicas - Total - R$ (milhões)': 'Credito'}, inplace=True)
juros.rename(columns={
             '20716 - Taxa média de juros das operações de crédito - Pessoas físicas - Total - % a.a.': 'Juros'}, inplace=True)

# Converter caracteres
selic.replace(',', '.', regex=True, inplace=True)
juros.replace(',', '.', regex=True, inplace=True)

# Converter valores para numérico
selic['Selic'] = pd.to_numeric(selic['Selic'], errors='coerce')
credito['Credito'] = pd.to_numeric(credito['Credito'], errors='coerce')
juros['Juros'] = pd.to_numeric(juros['Juros'], errors='coerce')

# Remove indices nulos
df = selic.dropna(subset=['Selic'], inplace=True)
df = juros.dropna(subset=['Juros'], inplace=True)
df = credito.dropna(subset=['Credito'], inplace=True)

# Unir datasets
df = selic.merge(juros, on='Data', how='inner')
df = df.merge(credito, on='Data', how='inner')


# Salvar dados processados
df.to_csv('data/processed/dados_processados.csv', sep=';',  index=False)
