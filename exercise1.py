###
###    Ejercicio 1
###

"""
Crear una función que reciba un número como argumento y devuelva
el largo de este número

Ejemplos:
number_length(10) -> 2
number_length(10000) -> 5
number_length(4321) -> 2

Restricciones:
El número no puede ser negativo
El número que se MANDA a la función tiene que ser tipo INT
No se puede utilizar el método length
"""

def length_number (number):
    if (number > 0):                                            # Verifico si es un número positivo.
        length = 0                                              # Inicializo la variable que guarda el largo del número.
        for i in range (100):                                   # Con un for hago una comparación iterativa para contar cuántos dígitos tiene el número.
            aux = 10 ** i
            a = number / aux
            if a > 1:
                length += 1
            else:
                break
        return f'El largo de {number} es', length               # De vuelvo el largo del número.
    else:
        return None, 'No se pueden utilizar números negativos'  # Se imprime un mensaje cuando el valor es negativo.

