import pandas as pd
df = pd.read_excel(r"C:\\Users\\jaque\Desktop\\global-analy\\data\\corruption_world.xlsx", engine='openpyxl')


print(df.columns)

df_first_four = df.iloc[:, :5]

print(df_first_four)

 