"""

17. Conversiones entre diferentes tipos de datos

"""

"""
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1), type(num2)) # Conversion implicita - Hecha automaticamente
"""

num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
edad = int(edad)
edadNueva = 1

print("Tu edad nueva es: ", edadNueva + edad)