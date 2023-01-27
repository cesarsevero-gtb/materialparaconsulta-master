import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
local,escala = 20,2



dados = np.ramdom.normal(loc=local, scale=escala, size=1000)
plt.hist(dados, color = "lightblue", ec="red")
