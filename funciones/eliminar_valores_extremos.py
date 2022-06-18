import math
import numpy as np

def eliminar_valores_extremos(binario, centroide, umbral):
    [f, c] = binario.shape
    resultado = binario.copy()
    for i in range(0, f):
        for j in range(0, c):
            if resultado[i][j] == 1:
                SE = math.sqrt((i-centroide[1])**2 + (j-centroide[0])**2)
                if SE >= umbral:
                    resultado[i][j] = 0
    return resultado