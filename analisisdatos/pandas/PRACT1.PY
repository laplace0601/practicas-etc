import pandas as pd
df = pd.read_csv(r"c:\Users\jesus\OneDrive\Documentos\proyectos\cosasramdonde python\dataframes\titanic.csv") #permite leer archivos csv

df = pd.read_csv("titanic.csv")  # Carga el archivo CSV en un DataFrame llamado df

print(df.shape)        # → Muestra una tupla con (número de filas, número de columnas)

print(df.head())       # → Muestra las primeras 5 filas del DataFrame, útil para inspección rápida

df.info()              # → Muestra información general del DataFrame:
                       #    - cantidad de entradas
                       #    - nombres y tipos de columnas
                       #    - cuántos valores no nulos tiene cada columna

print(df.describe())   # → Genera estadísticas descriptivas de las columnas numéricas:
                       #    - media, desviación estándar, mínimos, máximos, percentiles

print(df.describe(include="all"))  # → Igual que el anterior, pero incluye columnas no numéricas (como texto o categorías)
Usa mean() cuando los datos están distribuidos de forma simétrica.

Usa median() cuando hay valores atípicos o distribución sesgada.
df.loc #loc es pra crear condicionales de filtro, si quiero selecionar solo las frutas que hayan vendido mas de 20 unidades etc por nombres
df.iloc # este para indices iloc[0,1 :] por posicion numerica
