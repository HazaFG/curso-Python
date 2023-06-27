"""

46. Ciclo While
- Hazael Flores


"""

"""
monedas = 5

while(monedas > 0):
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("Ya no tengo monedas")
"""


"""
respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir?: (s/n): ")
else:
    print("Gracias")
"""

"""
respuesta = 's'

while respuesta == 's':
    pass

print("Hola")
"""

nombre = input("Tu nombre: ").lower()

for letra in nombre:
    if letra == 'z':
        break #continue
    print(letra)

