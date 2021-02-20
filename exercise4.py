###
###     Exercise 4
###

"""
Crear una función que devuelva un número con un formato específico

Ejemplos
format_number(1000) -> '1,000'
format_number(43214124) -> '43,214,124'

Restricciones
El argumento no puede ser negativo
El argumento debe ser entero

"""

def format_number(number):
  cadena = str(number)
  if len(cadena) > 3:
    list_digits = list(cadena)
    list_digits.reverse()
    for index in range(3, len(list_digits) + 1, 4):
      list_digits.insert(index, ',')
    list_digits.reverse()
  else:
    return cadena
  aux = ''
  for element in list_digits:
    aux += element
  return aux

###
###     Exercise 4.1
###

"""
Agregar el separador que el usuario indique

Ejemplos
format_number(1000, '#') -> '1#000'
format_number(43214124, '#') -> '43#214#124'

Restricciones
El argumento no puede ser negativo
El argumento debe ser entero

"""

def format_number_4_1(number, separator = ','):
  cadena = str(number)
  if len(cadena) > 3:
    list_digits = list(cadena)
    list_digits.reverse()
    for index in range(3, len(list_digits) + 1, 4):
      list_digits.insert(index, separator)
    list_digits.reverse()
  else:
    return cadena
  aux = ''
  for element in list_digits:
    aux += element
  return aux