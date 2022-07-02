import numpy as np
import cv2

def color2regionbinario(imagen, imagen_procesada):
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    Rojo = imagen_rgb[:,:,0]
    Verde = imagen_rgb[:,:,1]
    Azul = imagen_rgb[:,:,2]
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    negativo = imagen_procesada==0
    Rojo[negativo]  = imagen_gris[negativo]
    Verde[negativo] = imagen_gris[negativo]
    Azul[negativo]  = imagen_gris[negativo]
    resultado = np.zeros(imagen.shape, np.uint8)
    resultado[:,:,0] = Rojo
    resultado[:,:,1] = Verde
    resultado[:,:,2] = Azul
    return resultado