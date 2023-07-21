"""

63. Funciones dinamicas
- Hazael Flores


"""

"""
#Verificar si pasa de las 3 cifras este numero
def chequear_3_cifras(numero):
    return numero in range(100, 1000)

suma = 567 + 402

resultado = chequear_3_cifras(suma)
print(resultado)
"""

"""
palabra = 'odio_python_:D'

for a in palabra:
    print(a)
"""

"""
#Chequea todos los elementos de una lista
def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifras([555, 99, 600])
print(resultado)
"""


"""
#Ver los numeros de la lista
def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([555, 99, 600])
print(resultado)
"""


"""
def todos_positivos(lista_parametros):
    lista_vacia = []
    for valores in lista_parametros:
        if valores >= 0:
            #lista_vacia.append(valores)
            return True
        else:
            pass
    return lista_vacia

resultado = todos_positivos([-8, 99, 600])
print(resultado)
"""

def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero > 0 and numero < 1000:
            suma = suma + numero
    return suma

lista_numeros = [100, 250, 500, 750, 1200, 50, 800]

# Llamada a la función
resultado_suma = suma_menores(lista_numeros)
print(f"La suma de los números menores a 1000 es: {resultado_suma}")






