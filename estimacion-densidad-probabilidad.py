import numpy as np
from matplotlib import pyplot as plt
from numpy.random import normal
from scipy.stats import norm
from numpy import hstack
from sklearn.neighbors import KernelDensity

#estimacion parametrica
# samples = normal(loc=50, scale=5, size=10000) #mu=50, sigma=5
# mu = np.mean(samples)
# sigma = np.std(samples)
# dist = norm(mu, sigma)
# values = [value for value in range(30, 70)]
# probabilidades = [dist.pdf(value) for value in values]
# plt.hist(samples, bins=30, density=True)
# plt.plot(values, probabilidades)
# plt.show()

#estimacion no parametrica
samples1 = normal(loc=20, scale=5, size=300)
samples2 = normal(loc=40, scale=5, size=700)
samples = hstack((samples1, samples2))

model = KernelDensity(bandwidth=2, kernel='gaussian')
samples = samples.reshape((len(samples), 1))
model.fit(samples)

values = np.asarray([value for value in range(1, 60)])
values = values.reshape((len(values), 1))
probabilities = model.score_samples(values) #probabilidad logaritmica
probabilities = np.exp(probabilities) #invertir la probabilidad logaritmica
plt.hist(samples, bins=50, density=True)
plt.plot(values, probabilities)
plt.show()
