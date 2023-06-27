"""

52. Comprension de listas
- Hazael Flores


"""

"""
palabra = "python"

lista = [letra for letra in palabra]

print(lista)
"""
"""
lista = [letra for letra in 'python']
print(lista)
"""

"""
lista = [num if num * 2 > 10 else 'no' for num in range(0,21,2)]
print(lista)
"""

pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]

print(metros)


valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [num for num in valores if num%2 == 0]
print(valores_pares)

