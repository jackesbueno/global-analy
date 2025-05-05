import pandas as pd

# Lê o CSV
# Refrencia: https://www.kaggle.com/datasets/palinatx/mean-temperature-for-countries-by-year-2014-2022?resource=download
df = pd.read_csv("C:\\Users\\jaque\\Desktop\\global-analy\\data\\combined_temperature.csv", sep=",")

# Renomeia colunas para facilitar
df = df.rename(columns={
    "Country": "País",
    "Year": "Ano",
    "Annual Mean": "Temperatura_ºC"
})

# Temperaturas entre 0 e -25
df_temp_negativa = df[(df["Temperatura_ºC"] < 0) & (df["Temperatura_ºC"] >= -25)]

# Temperaturas entre 0 e 40
df_temp_positiva = df[(df["Temperatura_ºC"] >= 0) & (df["Temperatura_ºC"] <= 50)]

# Mantém apenas as colunas desejadas
colunas_desejadas = ["País", "Ano", "Temperatura_ºC"]
df_temp_negativa = df_temp_negativa[colunas_desejadas]
df_temp_positiva = df_temp_positiva[colunas_desejadas]

# Exibe os resultados
print("Temperaturas entre 0 e -25°C:")
print(df_temp_negativa)

print("\nTemperaturas entre 0 e 50°C:")
print(df_temp_positiva)
