"""

49. Zip
- Hazael Flores


"""

nombres = ["pepe", "pedro", "jose"]
edades = [45,40,87]
ciudades = ['Mexico', 'Madrid', 'Cordoba', 'Santiago']

combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} anos y vive en {ciudad}")
