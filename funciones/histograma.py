import matplotlib.pyplot as plt
import numpy as np

def imagen_histograma(imagen_gris):
  (f, c) = imagen_gris.shape
  histograma = np.zeros((1, 256))
  for i in range(0, f):
    for j in range(0, c):
      valor = imagen_gris[i][j]
      histograma[0][valor] = histograma[0][valor] + 1

  plt.plot(histograma[0])