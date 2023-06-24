"""

34.sets
- Hazael Flores

"""

"""
miSet = set([1,2,3,4,5]) #No importa si los datos se repiten
#print(len(miSet))

print(2 in miSet) #True o false

print(type(miSet))
print(miSet)
"""

"""    
s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2)
print(s3)

"""

s1 = {1,2,3}
s1.add(4)
s1.remove(3)
s1.discard(6) # Descartar no eliminar

s1.pop() #Aleatorio

s1.clear()

print(s1)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

azar = sorteo.pop()

print(sorteo)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)



