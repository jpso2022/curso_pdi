import numpy as np

def borde(imagen, umbral):
    (f, c) = imagen.shape
    #mascara
    Gx = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]])
    Gy = np.array([[-1, -1, -1],
                [0,   0,  0],
                [1,  1,  1]])
    # Ampliando la imagen
    (fm, cm) = Gx.shape
    I = 128*np.ones((f+2*fm, c+2*cm))
    I[fm:-fm, cm:-cm] = imagen

    #binario 
    resultado = np.zeros((f, c), np.ubyte)
    for i in range(0, f):
        for j in range(0, c):
            I2 = I[i:i+fm,j:j+cm]
            I3 = I2*Gx
            I4 = I2*Gy
            sum1 = abs(I3.sum())
            sum2 = abs(I4.sum())
            suma = sum1 + sum2
            if suma > umbral:
                resultado[i][j] = 1
            else:
                resultado[i][j] = 0
    return resultado