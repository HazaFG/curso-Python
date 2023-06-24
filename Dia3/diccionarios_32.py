"""

32. diccionarios
- Hazael Flores

"""

"""
diccionario = {'c1':'valor1', 'c2':'valor2'}
print(diccionario)

resultado = diccionario['c1']
print(resultado)
"""

"""
cliente = {"nombre":'Hazael', 'apellido':"Flores", 'Peso':90, 'Talla':1.89}
consulta = cliente['Talla']
print(consulta)
"""

"""
dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'][1]) #Imprime el numero 20
print(dic['c3']['s1']) #Imprime el numero 100
"""

#IMPRIMIR LA e de c2 pero en Mayuscula

"""
dic = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dic['c2'][1].upper())
"""

dic = {1:'a', 2:'b'}
print(dic)

#Podemos agregar nuevos elementos a nuestro diccionario
dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)

print(dic.keys()) #Trae solo las lavves
print(dic.values()) #Trae los valores
print(dic.items()) #SE TRAE TODOO


mi_dic = {'nombre':'Karen', 'apellido':'Jurgens', 'edad':35, 'ocupacion':'Periodista'}


mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'

print(mi_dic)


