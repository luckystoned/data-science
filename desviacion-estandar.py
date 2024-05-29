import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Data Science/cars.csv')

# Desviacion Estandar
DesviacionEstandar = df['price_usd'].std()
print(DesviacionEstandar)

# Rango = valor maximo - valor minimo
Rango = df['price_usd'].max() - df['price_usd'].min()
print(Rango)

# Quartiles
Median = df['price_usd'].median()
Q1 = df['price_usd'].quantile(q=0.25)
Q3 = df['price_usd'].quantile(q=0.75)
min_val = df['price_usd'].quantile(q=0)
max_val = df['price_usd'].quantile(q=1.0)
print(min_val, Q1, Median, Q3, max_val)


iqr = Q3 - Q1
print(iqr)

# Outliers
minlimit = Q1 - 1.5 * iqr
maxlimit = Q3 + 1.5 * iqr
print(minlimit, maxlimit)

# Diagrama de Caja
sns.boxplot(x=df['price_usd'])
sns.boxplot(x='engine_fuel', y='price_usd', data=df)
