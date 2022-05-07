import numpy as np

# funcion para aumentar el contraste
def contraste(imagen):
  (f, c) = imagen.shape
  persona_contraste = np.zeros((f, c))
  maximo = imagen.max()
  minimo = imagen.min()
  for i in range(0, f):
    for j in range(0, c):
      pixel_actual = imagen[i][j]
      persona_contraste[i][j] = round(((pixel_actual - minimo) / (maximo - minimo)) * 255)
      persona_contraste[i][j] = persona_contraste[i][j] + 30
      if persona_contraste[i][j] > 255:
        persona_contraste[i][j] = 255
      elif persona_contraste[i][j] < 0:
        persona_contraste[i][j] = 0
  return persona_contraste.astype(np.uint8)
