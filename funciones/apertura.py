from curso_pdi.funciones.dilatacion import dilatacion
from curso_pdi.funciones.erosion import erosion

def apertura(imagen, elemento_estructural):
  imagen_erosionada = erosion(imagen, elemento_estructural)
  imagen_dilatada = dilatacion(imagen_erosionada, elemento_estructural)
  return imagen_dilatada