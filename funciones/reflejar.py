import numpy as np

def reflejar_imagen(imagen_gris):
  (f, c) = imagen_gris.shape
  d = len(imagen_gris.shape)
  imagen_reflejada = np.zeros((f, c))
  if d == 2:
    for i in range(0, f):
      for j in range(0, c):
        imagen_reflejada[i][j] = imagen_gris[i, c-(j+1)]

  return imagen_reflejada.astype(np.uint8)