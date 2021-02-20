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
  if not(isinstance(number, int)): #Comparo si number es del tipo int
    return 'El primer parámetro debe ser únicamente un número entero positivo'
  if not(isinstance(length_index, int)): #Comparo si length_index es del tipo int
    return 'El segundo parámetro debe ser únicamente un número entero positivo'
  if number < 0 or length_index < 0: #Comparo si ambos parámetros son mayores que cero
    return 'Esta función sólo acepta números mayores que cero'
  return [number * i for i in range(1, length_index + 1)]