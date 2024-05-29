import numpy as np
import numpy.random as binomial
from scipy.stats import binom
from math import factorial
import matplotlib.pyplot as plt

# Definimos la distribución binomial
def my_binomial(k, n, p):
    return factorial(n) / (factorial(k) * factorial(n - k)) * pow(p, k) * pow(1 - p, n - k)


print(my_binomial(2, 3, 0.5))

# Usando la librería numpy
dist = binom(3, 0.5)
print(dist.pmf(2))

# Ejericio: Calcular P(k<=2, n=3, p=0.5) con la funcion de distribucion acumulada
print(dist.cdf(2))

#Simulador de secuencias con generador de números aleatorios
# ejecutar varias veces para ver como cambia la secuencia
p=0.5
n=3
print(binomial.binomial(n, p))

arr = []
for _ in range(100):
    arr.append(binomial.binomial(n, p))

print(arr)

def plot_hist(num_trials):
    values = [0, 1, 2, 3]
    arr = []
    for _ in range(num_trials):
        arr.append(binomial.binomial(n, p))
    sim = np.unique(arr, return_counts=True)[1] / len(arr)
    teorica = [dist.pmf(k) for k in values]
    plt.bar(values, sim, color='red')
    plt.bar(values, teorica, alpha=0.5, color='blue')
    plt.title('{} experimentos'.format(num_trials))
    plt.show()

plot_hist(20000)





