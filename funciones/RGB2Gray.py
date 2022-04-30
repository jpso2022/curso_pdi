import numpy as np

def ConvertRGB2Gray(imagen_rgb):
  d = len(imagen_rgb.shape)
  if d == 3:
    R = imagen_rgb[:,:, 0]
    G = imagen_rgb[:,:,1]
    B = imagen_rgb[:,:,2]
    imagen_rgb_gris = 0.3013*R + 0.5897*G + 0.109*B
    return imagen_rgb_gris.astype(np.uint8)