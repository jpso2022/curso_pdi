from curso_pdi.funciones.dilatacion import dilatacion
from curso_pdi.funciones.erosion import erosion

def cierre(imagen, elemento_estructural):
  imagen_dilatada = dilatacion(imagen, elemento_estructural)
  imagen_erosionada = erosion(imagen_dilatada, elemento_estructural)
  return imagen_erosionada