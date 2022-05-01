import numpy as np

def brillo(imagen, factor_correccion):
  (f, c) = imagen.shape
  persona_brillo = np.zeros((f, c))
  for i in range(0, f):
    for j in range(0, c):
      persona_brillo[i][j] = imagen[i][j] + factor_correccion
      if persona_brillo[i][j] > 255:
        persona_brillo[i][j] = 255
      elif persona_brillo[i][j] < 0:
        persona_brillo[i][j] = 0
  return persona_brillo.astype(np.uint8)
