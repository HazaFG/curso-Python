"""

55. Proyecto
- Hazael Flores


La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:

     - Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
    un número que no está permitido.

    - Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
    decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.

    - Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
    misma manera.

    - Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
    intentos le ha tomado.

Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos.

"""

print("\n------------------------------------ PROYECTO DIA 4 -------------------------------------------- ")

from random import *

nombre = (input("\nHola, Ingresa tu nombre por favor: "))
print(f"\nOkey {nombre}, mira, tienes que adivinar un numero entre 1 y 100\ny desgraciadamente solo tienes 8 intentos")

aleatorio = randint(1 , 100)
#print(aleatorio)
intentos = 0

juego = True

while(juego):
    numero = int(input("\nIngresa un numero para adviniar: "))

    if(numero < 1 or numero > 100):
        intentos +=1
        print(f"Numero invalido, te quedan {intentos} intentos")
    elif(numero < aleatorio):
        intentos +=1
        print(f"El numero {numero} es menor al numero aleatorio que hay que adivinar, llevas {intentos} intentos")
    elif(numero > aleatorio):
        intentos +=1
        print(f"El numero {numero} es mayor al numero aleatorio que hay que adivinar, llevas {intentos} intentos")
    elif(numero == aleatorio):
        intentos +=1
        print(f"Felicidades {nombre}, el numero a adivinar si es: {aleatorio}")
        juego = False
    if(intentos == 8):
        print("Perdiste, se te acabaron todos los intentos!")
        print(f"El numero era: {aleatorio}")
        juego = False





