import requests
import pandas as pd
import numpy as np

# Função para obter os dados do indicador
def get_indicator_data(indicator, country_code):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?format=json&per_page=1000"
    response = requests.get(url)
    data = response.json()

    records = []
    for item in data[1]:
        if item['value'] is not None:
            records.append({
                'year': int(item['date']),
                indicator: item['value']
            })

    return pd.DataFrame(records)

# Função para obter o nome do país
def get_country_name(country_code):
    url = f"http://api.worldbank.org/v2/country/{country_code}?format=json"
    response = requests.get(url)
    data = response.json()
    return data[1][0]['name']

# Indicadores
indicator_gdp = "NY.GDP.PCAP.CD"     # PIB per capita
indicator_gini = "SI.POV.GINI"       # Índice de Gini

# Código do país (ex: Brasil = 'BR')
country_code = "US"

# Obter nome do país
country_name = get_country_name(country_code)

# Dados individuais
df_gdp = get_indicator_data(indicator_gdp, country_code)
df_gini = get_indicator_data(indicator_gini, country_code)

# Unir os dois dataframes pelo ano
df_merged = pd.merge(df_gdp, df_gini, on="year", how="inner")

# Renomear colunas para clareza
df_merged.columns = ["Ano", "PIB_per_capita", "GINI"]

# Adicionar nome do país antes da coluna 'Ano'
df_merged['Pais'] = country_name
df_merged = df_merged[['Pais', 'Ano', 'PIB_per_capita', 'GINI']]

# Exibir o DataFrame com as colunas necessárias
print(df_merged[['Pais', 'Ano', 'PIB_per_capita', 'GINI']])
