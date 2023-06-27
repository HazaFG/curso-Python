"""

45. Ciclo For
- Hazael Flores


"""

"""
lista = ['a', 'b', 'c', 'd']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")
"""

"""
lista = ['Andrea', 'Hazael', 'Yuniva', 'Abdiel']

for nombre in lista:
    if nombre.lower().startswith('a'):
        print(nombre)
    else:
        print("No coincide")
"""

"""
numeros = [1,2,3,4,5]
valor = 0

for numero in numeros: # Numero agarra el valor literalmente de numeros, vaya ciclo mas raro es esta mierd*
    valor = valor + numero

print(valor)
"""

"""
palabra = 'odio_python_:D'

for a in palabra:
    print(a)
"""

"""
for a in 'python':
    print(a)
"""

"""
for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)
"""

"""
for a,b in [[1,2], [3,4], [5,6]]: #Listas dentro de listas
    print(a)
    print(b)
"""

#VAMOS A ITERAR EN UN DICCIONARIO

# Al ejecutar este bloque de codigo solo se imprimen las llaves del diccionario, mas no el contenido

"""
dic = {'clave1': 'a', 'clave2': 'b', 'clave3':'c'}

for item in dic:
    print(item)
"""

#Vamos a hacer que se pueda imprimir los items dentro de cada diccionario
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic.items(): #dic.values() para ver los valores de los diccionarios
    print(item)


