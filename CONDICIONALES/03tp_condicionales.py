#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor o igual a 6, deberá mostrar un mensaje en pantalla que diga "Es mayor de edad"

edad = int (input("Ingrese su edad:"))

if edad > 18:
    print ("Es mayor de edad")

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga "Aprobado"; en caso contrario deberá mostrar el mensaje "Desaprobado".

nota = int (input ("Ingrese su nota:"))

if nota >= 6: 
    print ("Aprobado")
else:
    print ("Desaprobado")

#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un npumero par, imprimir en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un npumero par".

int (input ("Ingrese un número:"))

if número %2== 0:
    print ("Ha ingresado un número par:")
else:
    print ("Por favor, ingrese un número par")

#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: -Niño/a: menor de 12 años. -Adolescente: mayor o igual que 12 años y menor que 18 años. -Adulto/a joven: mayor o igual que 18 años y menor que 30 años. -Adulto/a: mayor o igual que 30 años.

edad = int (input("Ingrese su edad:"))

if edad < 12:
    print ("Niño/a menor de 12 años")
