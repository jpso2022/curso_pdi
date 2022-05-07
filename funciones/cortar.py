import numpy as np

# funcion para cortar imagenes
def cortar_imagen(imagen_gris, inicio_x, inicio_y, alto, ancho):
  (f, c) = imagen_gris.shape  
  d = len(imagen_gris.shape)
  if d == 2:
    imagen_cortada = imagen_gris[inicio_y:inicio_y+alto, inicio_x:inicio_x+ancho]
    return imagen_cortada.astype(np.uint8)