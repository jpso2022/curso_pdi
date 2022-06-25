import numpy as np
import math

def filtro_mean(imagen, mask):
    (fs, cs) = mask.shape
    fss = fs/2
    css = cs/2

    # Redondeos
    fss2 = math.floor(fss)
    css2 = math.floor(css)
    fss1 = math.ceil(fss)
    css1 = math.ceil(css)

    # Dimensión de la imagen
    (fi, ci) = imagen.shape

    # Dimensión de la imagen ampliada
    f = fi + fss2 + fss1
    c = ci + css2 + css1

    # Ampliando la imagen
    imagen_ampliada = 128*np.ones((f,c))
    imagen_ampliada[fss2:f-fss1, css2:c-css1] = imagen

    resultado = np.zeros((fi, ci), np.uint8)
    for i in range(0, fi):
        for j in range(0, ci):
            # Es una porción segun el elemento estructural
            I2 = imagen_ampliada[i:fs+i,j:cs+j]
            resultado[i][j] = np.mean(I2)
        
    return resultado