"""

37. Proyecto
- Hazael Flores

La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.

2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todoO el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.

3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.

4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.

5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta.

"""

print("\n------------------------------------ PROYECTO DIA 3 -------------------------------------------- ")

texto = (input("\nIngresa un texto que se te de la gana: ").lower())
letraUno = (input("Ingresa la primer letra que quieras: ").lower())
letraDos = (input("Ingresa la segunda letra que quieras: ").lower())
letraTres = (input("Ingresa la tercer letra que quieras: ").lower())
lista_caracteres = list(texto)

# PUNTO NUMERO 1
caja = texto.count(letraUno)
caja2 = texto.count(letraDos)
caja3 = texto.count(letraTres)

print(f"\nLa letra {letraUno} aparece {caja} veces")
print(f"La letra {letraDos} aparece {caja2} veces")
print(f"La letra {letraTres} aparece {caja3} veces")

#PUNTO NUMERO 2
palabras = texto.split()
cantidadPalabras = len(palabras)

print(f"\nLa cantidad de palabras en el texto es: {cantidadPalabras}")

#PUNTO NUMERO 3
primera_letra = lista_caracteres[0]
ultima_letra = lista_caracteres[-1]

print("La primer letra es: ", primera_letra)
print("La ultima letra es ", ultima_letra)

#PUNTO NUMERO 4
lista_caracteres.reverse()
palabras.reverse()

lista_caracteres = ' '.join(palabras)
print("\nLa lista invertida: ", lista_caracteres)

#PUNTO NUMERO 5
resultado = "python" in texto
respuestas = {True: "\nLa palabra 'Python' se encuentra en el texto.", False: "\nLa palabra 'Python' no se encuentra en el texto."}
print(respuestas[resultado])

