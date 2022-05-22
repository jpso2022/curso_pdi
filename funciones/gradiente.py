from curso_pdi.funciones.dilatacion import dilatacion
from curso_pdi.funciones.erosion import erosion

def gradiente(imagen, elemento_estructural):
  imagen_dilatada = dilatacion(imagen, elemento_estructural)
  imagen_erosionada = erosion(imagen, elemento_estructural)
  resultado = abs(imagen_dilatada - imagen_erosionada)
  return resultado