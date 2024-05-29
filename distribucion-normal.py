import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Distriución gaussiana
# def gaussian(x, mu, sigma):
#     return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2))

# x = np.arange(-4, 4, 0.1)
# y = gaussian(x, 0, 2)

# plt.plot(x, y)

# #Distribución normal
# dist = norm(0, 1)
# xdn = np.arange(-4, 4, 0.1)
# ydn = [dist.pdf(value) for value in x]

# plt.plot(xdn, ydn)

#Distribución normal acumulada
# distAcum = norm(0, 1)
# xAcum = np.arange(-4, 4, 0.1)
# yAcum = [distAcum.cdf(value) for value in x]

# plt.plot(xAcum, yAcum)

#Distribución normal gaussiana a partir de datos
df = pd.read_excel('Data Science/s057.xls')
arr = df['Normally Distributed Housefly Wing Lengths'].values[4:]
# values, dist = np.unique(arr, return_counts=True)
# plt.bar(values, dist)

# Estimacion de la distribución
mu = np.mean(arr)
sigma = np.std(arr)
x = np.arange(30, 60, 0.1)
dist = norm(mu, sigma)
y = [dist.pdf(value) for value in x]
plt.plot(x, y, color='red')
values, dist = np.unique(arr, return_counts=True)
plt.bar(values, dist/len(arr), alpha=0.5)


