###
###     Exercise 2
###

"""
Crear una función que reciba dos números como argumentos
            (número, longitud)
y devolver una lista con los múltiplos del número dada la longitud

Ejemplos
list_of_multiples(7, 5) -> [7, 14, 21, 28, 35]
list_of_multiples(17, 6) -> [17, 34, 51, 68, 85, 102]

Restricciones:
Los argumentos no pueden ser negativos
Los argumentos deben ser enteros
"""

def list_of_multiples(number, length_index):
  if type(number) != int or type(length_index) != int or number < 0 or length_index < 0 :
    return 'Necesitas ingresar únicament números enteros positivos'
  return [number * i for i in range(1, length_index + 1)]