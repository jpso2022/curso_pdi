from curso_pdi.funciones.erosion import erosion

def perimetro(imagen, elemento_estructural):
  imagen_erosionada = erosion(imagen, elemento_estructural)
  resultado = imagen - imagen_erosionada
  return resultado