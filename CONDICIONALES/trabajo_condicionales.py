#Ejercicio 1
edad = int (input ("Ingrese su edad:"))

if edad > 18:
    print ("Es mayor de edad")

#Ejercicio 2

nota = int (input("Ingrese su nota:"))

if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#Ejercicio 3

número = int (input ("Ingresar un número par:"))

if número % 2 == 0:
    print ("Ha ingresado un número par.")
else:
    print ("Por favor, ingrese un número par.") 

#Ejercicio 4

edad = int(input("Ingrese su edad:"))

if edad < 12:
    print ("Categoría: Niño/a.")
elif edad >= 12 and edad <  18:
    print ("Categoría: Adolescente.")
elif edad >= 18 and edad < 30:
    print ("Categoría: Adulto/a joven.")
else:
    print ("Adulto/a.")

#Ejercicio 5

contraseña = input ("Introduzca una contraseña de entre 8 y 14 caracteres: ")
longitud = len (contraseña)

if longitud <=8 and longitud >=14:
    print ("Ha ingresado una contraseña correcta.")
else:
    print ("Por favor, ingrese una contraseña entre 8 y 14 caracteres.")

#Ejercicio 6

import random
import statistics

numeros_aleatorios = [random.randint (1, 100) for i in range (50)]
from statistics import mode, median, mean
mean (numeros_aleatorios)

moda = statistics.mode (numeros_aleatorios)
mediana = statistics.median (numeros_aleatorios)
media = statistics.mean (numeros_aleatorios)

if media > mediana and mediana > moda:
    print ("Sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo o a la izquierda.")
else:
    print ("Sin sesgo.")

#Ejercicio 7

texto = input ("Ingrese una frase o palabra:")
vocales = "aeiouAEIOU"

if texto and texto [-1] in vocales:
    texto += "!"
print (texto)

#Ejercicio 8

nombre = input ("Ingrese su nombre:")

print ("Elija la opción:")
print ("1. Mostrar el nombre en MAYÚSCULAS")
print ("2. Mostrar el nombre en minúsculas")
print ("3. Mostrar el nombre con la primera letra en mayúscula")

opcion = input ("Ingrese el número de la opción (1, 2 o 3):")

if opcion == "1":
    print ("Resultado:", nombre.upper())
elif opcion == "2":
    print ("Resultado:", nombre.lower())
elif opcion == "3":
    print ("Resultado:", nombre.title())
else:
    print ("Opción no válida")

#Ejercicio 9

magnitud = float (input("Ingrese la magnitud del terremoto en la escala de Richter:"))

if magnitud <3:
    print ("Muy leve.")
elif magnitud >= 3 and magnitud < 4: 
    print ("Leve.")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte") 
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte")
else:
    print ("Extremo")

#Ejercicio 10

hemisferio = input ("¿En qué hemisferio se encuentra (N/S):").upper()
mes = input ("¿Qué mes del año es?").lower()
día = int (input ("¿Qué día es?:"))

if hemisferio == "N":
    if (mes=="diciembre" and día >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and día <= 20):
        estacion = "Invierno"
    elif (mes == "marzo" and día >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and día <=20):
        estacion = "Primavera"
    elif (mes == "junio" and día >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and día <= 20):
        estacion = "Verano"
    elif (mes == "septiembre" and día >= 21) or mes == "octubre" or mes == "noviembre" (mes == "diciembre" and día <= 20):
        estacion = "Otono"
    else:
        estacion = "Fecha inválida para el hemisferio Norte"
elif hemisferio == "S":
    if (mes == "diciembre" and día >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and día <= 20):
        estacion = "Verano"
    elif (mes == "marzo" and día >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and día <=20):
        estacion = "Otoño"
    elif (mes == "junio" and día >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and día <= 20):
        estacion = "Invierno"
    elif (mes == "septiembre" and día >= 21) or mes == "octubre" or mes == "noviembre" (mes == "diciembre" and día <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida para el hemisferio Sur"
else:
    estacion = "Hemisferio inválido. Por favor, ingrese N o S."
