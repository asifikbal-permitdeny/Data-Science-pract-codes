import pandas as pd
df=pd.read_excel('rough.xlsx')
print(df.head())


df.dropna(axis=0,inplace=True)

print(df)

print(df.info())

print(df.describe())