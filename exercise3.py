###
###     Exercise 3
###

"""
Crear una función que devuelva el factorial de un número

Ejemplos
factorial(3) -> 6 (3*2*1)
factorial(4) -> 24 (4*3*2*1)

"""
### Sin Recursividad
def factorial_sn_rec(number):
    if not(isinstance(number, int)) : # Comparo si el parámetro introducido es int
        return 'El parámetro debe ser únicamente un número entero positivo'
    if number < 0 : # Comparo si el número es un entero positivo
        return 'Esta función sólo acepta números mayores que cero'
    fac = 1 # Inicio una variable auxiliar para cargar el factorial
    if number == 0: # Si el usuario ingresa 0 entonces le devuelve 1
        return fac
    for i in range(1, number + 1): # Ciclo para calcular el factorial
        fac *= i
    return fac

### Con recursividad
def factorial(number):
    if not(isinstance(number, int)) : # Comparo si el parámetro introducido es int
        return 'El parámetro debe ser únicamente un número entero positivo'
    if number < 0 : # Comparo si el número es un entero positivo
        return 'Esta función sólo acepta números mayores que cero'
    if number == 0: # Si el usuario ingresa 0 entonces le devuelve 1
        return 1
    else : # Inicia el ciclo recursivo.
        return number * factorial(number - 1)