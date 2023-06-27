"""

51. Random
- Hazael Flores


"""

#from random import randint
from random import *

"""
aleatorio = randint(1 , 50)
print(aleatorio)
"""

"""
aleatorio = round(uniform(1,5), 1)
aleatorio = random()
print(aleatorio)
"""

"""
colores = ["Verde", "Rojo", "Azul", "Amarillo", "Morado"]
aleatorio = choice(colores)
print(aleatorio)
"""

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)




