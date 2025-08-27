print ("Hola mundo!")

nombre = input ("Por favor, ingrese su nombre: ")
print (f"Hola {nombre}!")

nombre = input ("Por favor, ingrese su nombre: ")
apellido = input ("Por favor, ingrese su apellido: ")
edad = input ("Por favor, ingrese su edad: ")
lugar_de_residencia = input ("Por favor, ingrese su lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} y vivo en {lugar_de_residencia}")

import math
radio = float(input("Ingrese el radio del círculo: "))
área = math.pi *radio ** 2
perímetro = 2 * math.pi *radio
print (f"El área del círculo es: {área:2})")
print (f"El perímetro del círculo es: {perímetro: 2}")

segundos = int (input ("Ingrese la cantidad de segundos: "))
horas = segundos / 3600 
print (f"{segundos} segundos equivalen a {horas: 2f} horas")

número = int (input ("Ingrese un número"))
print (f"\nTabla de multiplicar del {número}:")
for i in range(1,11):
    print (f"{número} x {i} = {número * i}")

num1 = int (input ("Ingrese el primer número entero (distinto de 0):"))
num2 = int (input ("Ingrese el segundo número entero (distinto de 0)"))
if num1 == 0 or num2 == 0:
    print("Error: los números deben ser distintos de 0.")
else:
    suma = num1 + num2
    división = num1 / num2
    multiplicación = num1 * num2
    resta = num1 - num2
print (f"Suma: {suma}")
print (f"División: {división: 2f}")
print (f"Multiplicación: {multiplicación}")
print (f"Resta: {resta}")

peso = float (input ("Ingrese su peso en kilogramos:"))
altura = float (input ("Ingrese su altura en metros:"))
imc = peso / (altura ** 2)
print (F"Su índice de Masa Corporal (IMC) es: {imc:.2f}")

celsius = float (input ("Ingrese la temperatura en grados Celsius:"))
fahrenheit = (9/5) * celsius + 32
print (f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

num1 = float (input ("Ingrese el primer número:"))
num2 = float (input ("Ingrese el segundo número:"))
num3 = float (input ("Ingrese el tercer número:"))
promedio = (num1 + num2 + num3) / 3
print (f"El promedio de los tres números es: {promedio:.2f}")