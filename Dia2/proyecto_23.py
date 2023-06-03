"""

23. Proyecto
- Hazael Flores

"""

nombre = (input("Como te llamas?: "))
dinero = input("Cuanto dinero has ganado en el ultimo mes?: ")
dinero = float(dinero)

#print(type(dinero))

total = ((dinero*0.13)+dinero)
round(total, 3)
print(f"Okey {nombre} Vas a ganar: {total}, tu comision fue de {dinero*0.13}")


