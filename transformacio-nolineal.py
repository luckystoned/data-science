import pandas as pd
import numpy as np

df = pd.read_csv('Data Science/cars.csv')

# df.price_usd.hist()

#Transformacion con tangente hiperbolica
p = 10000
df.price_usd.apply(lambda x: np.tanh(x/p)).hist()

