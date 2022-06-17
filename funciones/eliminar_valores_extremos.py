import math
import numpy as np

def eliminar_valores_extremos(binario, centroide, umbral):
    [f, c] = binario.shape
    resultado = np.zeros(binario.shape, np.uint8)
    for i in range(0, f):
        for j in range(0, c):
            if binario[i][j] == 1:
                SE = math.sqrt((i-centroide[1])**2 + (j-centroide[0])**2)
                if SE >= umbral:
                    binario[i][j] = 0
    return binario