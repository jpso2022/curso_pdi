import math
import numpy as np

def erosion(imagen_gris, elemento_estructural):
    (fs, cs) = elemento_estructural.shape
    fss = fs/2
    css = cs/2

    # Redondeos
    fss2 = math.floor(fss)
    css2 = math.floor(css)
    fss1 = math.ceil(fss)
    css1 = math.ceil(css)

    # Dimensión de la imagen_gris
    (fi, ci) = imagen_gris.shape

    # Dimensión de la imagen ampliada
    f = fi + fss2 + fss1
    c = ci + css2 + css1

    # Ampliando la imagen
    imagen_ampliada = 255 * np.ones((f,c))
    imagen_ampliada[fss2:f-fss1, css2:c-css1] = imagen_gris

    eros = np.zeros((fi, ci), np.uint8)
    # Aplicar la tecnica de erosion
    for i in range(0, fi):
        for j in range(0, ci):
            # Es una porción segun el elemento estructural
            I1 = imagen_ampliada[i:fs+i,j:cs+j]
            I2 = I1*elemento_estructural
            eros[i][j] = I2.min()
        
    return eros