import timeit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

X, y = datasets.load_diabetes(return_X_y=True)
raw = X[:, None, 2]

# reglas de escalamiento
max_raw = max(raw)
min_raw = min(raw)
sclaed = (2*raw - max_raw - min_raw)/(max_raw - min_raw)

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].hist(raw)
axs[1].hist(sclaed)

# modelos de escalamiento
def train_raw():
    linear_model.LinearRegression().fit(raw, y)

def train_scaled():
    linear_model.LinearRegression().fit(sclaed, y)

raw_time = timeit.timeit(train_raw, number=100)
scaled_time = timeit.timeit(train_scaled, number=100)

print('Tiempo de entrenamiento con datos originales: ', raw_time)
print('Tiempo de entrenamiento con datos escalados: ', scaled_time)


# z-score scaling

mean_raw = np.mean(raw)
std_raw = np.std(raw)
z_score = (raw - mean_raw)/std_raw

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].hist(raw)
axs[1].hist(z_score)

def train_z_score():
    linear_model.LinearRegression().fit(z_score, y)

def train_scaled_z():
    linear_model.LinearRegression().fit(sclaed, y)

z_score_time = timeit.timeit(train_z_score, number=100)
scaled_time_z = timeit.timeit(train_scaled_z, number=100)

print('Tiempo de entrenamiento con datos originales: ', z_score_time)
print('Tiempo de entrenamiento con datos escalados: ', scaled_time_z)
