#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
for i in range (0, 101):
    print (i)

#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 
numero =int (input("Ingresa un número entero:"))

if numero == 0:
    cantidad=1
else:
    numero= abs(numero)
    cantidad = 0

while numero > 0:
    numero//=10
    cantidad += 1
print ("El numero ingresado tiene", cantidad, "digito(s).")

#Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
a= int (input ("Ingresa el primer número entero:"))
b= int (input ("Ingresa el segundo número entero:"))

menor = min (a,b)
mayor = max (a,b)

suma = sum (range (menor + 1, mayor))

print (f"La suma de los números enteros entre {a} y {b}, excluyendo esos dos valores, es: {suma}")

#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
suma = 0
print ("Ingrese números enteros (0 es para finalizar):")

while True:
    número = int(input("Número:"))
    if número == 0:
        break
    suma += número

print (f"\n El total acumulado es:{suma}")

#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron encesarios para acertar el número.

import random

numero_secreto = random.randint (0,9)

intentos = 0
acertado = False

print ("Adivina el número entre 0 y 9")

while not acertado:
    intento = int(input("Ingresa tu número:"))
    intentos += 1
    if intento == numero_secreto:
        acertado = True
        print (f"¡Correcto! El número era {numero_secreto}.")
        print (f"Necesitaste {intentos} intentos.")
    else:
        print ("No es el número, intenta de nuevo.")

#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for numero in range (100, -1, -2):
    print (numero)

#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario
n = int (input ("Ingrese un número entero positivo:"))

if n < 0: 
    print ("Debe ingresar un número positivo.")
else: 
    suma = n* (n+1)//2
    print (f"La suma de los números entre 0 y {n} es: {suma}")

#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

def main ():
    cantidad = 100
    pares = 0
    impares= 0
    positivos = 0
    negativos = 0

    print (f"Ingrese {cantidad} números enteros:")

    for i in range (cantidad):
        número = int (input (f"Número {i+1}:"))

        if número % 2 == 0:
            pares += 1
        else:
            impares += 1

        if número >0:
            positivos += 1
        elif número <0:
            negativos += 1

    print ("\n--- Resultados ---")
    print ("Cantidad de pares:", pares)
    print ("Cantidad de impares:", impares)
    print ("Cantidad de positivos:", positivos)
    print ("Cantidad de negativos:", negativos)

main ()

#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando un solo valor).
def main ():
    cantidad = 100
    suma = 0

    print (f"Ingrese {cantidad} números enteros:")
    for i in range (cantidad):
        número = int(input(f"Número {+1}:"))
        suma += suma / cantidad

    print ("\n---Resultado---") 
    print ("La media de los números ingresados es:", media)

main ()
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

def main ():
    número = inpt("Ingrese un número entero:")
    invertido = número [::-1]

print (f"Número invertido", invertido)

main()
