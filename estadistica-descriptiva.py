import pandas as pd
import seaborn as sns

df = pd.read_csv('Data Science/cars.csv')
#df.dtypes
#df.describe() # Estadistica descriptiva

# create a frequency table for the number of engine_capacity values
#df['engine_capacity'].value_counts()


Promemedio = df['price_usd'].mean() # Promedio
Media = df['price_usd'].median() # Mediana

#Histograma = df['price_usd'].plot.hist(bins=20) # Histograma

#HistogramaSns = sns.displot(df, x = 'price_usd', hue = 'manufacturer_name') # Histograma con seaborn

#HistogramaSnsEngine = sns.displot(df, x = 'price_usd', hue = 'engine_type', multiple='stack') # Histograma con seaborn

#MotorType = df.groupby('engine_type').count() # Agrupar por tipo de motor

Q7_df = df[(df['manufacturer_name'] == 'Audi') & (df['model_name'] == 'Q7')]# Filtrar por marca y modelo
sns.displot(Q7_df, x = 'price_usd', hue = 'year_produced') # Histograma con seaborn
