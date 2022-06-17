import numpy as np

def vecino_cercano(imagen, filas, columnas):
    (f, c) = imagen.shape
    resultado = np.zeros((filas,columnas),np.uint8)
    for i in range(0, filas):
        i0 = round(f/filas*i)
        if 0<=i0<=f:
          for j in range(0, columnas):
              j0 = round(c/columnas*j)
              if 0<=j0<=c:
                  resultado[i][j] = imagen[i0, j0]
    return resultado