"""

59. Metodos
- Hazael Flores


"""

dic = {'clave1':100, 'clave2':500}

a = dic.popitem()
print(a)
print(dic)

"""
cadena = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
nueva_cadena = cadena.lstrip(", : % _ #")
print(nueva_cadena)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
a = frutas.insert(3, 'naranja')
print(frutas)

"""

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

resultado = marcas_smartphones.isdisjoint(marcas_tv)
print(resultado)