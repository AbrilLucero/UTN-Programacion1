#Ejercicio 1

def imprimir_hola_mundo ():
    print ("Hola Mundo!")

imprimir_hola_mundo ()

#Ejercicio 2
'''
Crear una función llamada saludar_usuario(nombre) que reciba
 como parámetro un nombre y devuelva un saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
 principal solicitando el nombre al usuario.
'''
def saludar_usuario (nombre):
    print (f"Hola {nombre} !")

nombre = input("Ingrese su nombre:")

saludar_usuario (nombre)

#Ejercicio 3
'''
Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados.
'''

def informacion_personal (nombre, apellido, edad, residencia):
    print (f"Soy {nombre}, tengo {edad} años y vivo en {residencia}.")

nombre = input ("Ingrese su nombre:")
apellido = input ("Ingrese su apellido:")
edad = int ( input ("Ingrese su edad:"))
residencia = input ("Ingrese su residencia:")

informacion_personal (nombre, apellido, edad, residencia)

#Ejercicio 4
'''
Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados.
'''
from math import pi
def calcular_area_circulo (radio):
    #a = pi * (r**2)
    return (pi * (radio**2))

def calcular_perimetro_circulo (radio):
    #p = 2* pi * r
    return (2*pi*radio)

radio = int (input("Ingrese el radio del círculo:"))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Area: {area}, perímetro {perimetro}")

#Ejercicio 5

'''
Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y 
 mostrar el resultado usando esta función.
'''

def segundos_a_horas (segundos):
    horas = segundos / 3600 #1hora equivale a 3600 seg
    return horas

segundos = float (input ("Ingrese la cantidad de segundos:"))

resultado = segundos_a_horas (segundos)

print ("Esto equivale a",resultado , "horas")

#Ejercicio 6

'''
Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción.
'''

def tabla_multiplicar (numero) :
    for x in range (11):
        print(f"{numero} * {x} = {numero*x}")

numero = int (input ("Ingrese un número:"))

tabla_multiplicar (numero)

#Ejercicio 7

'''
Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resultado 
 de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara.
'''

def operaciones_basicas (a, b):
    suma = a + b
    resta = a - b
    multiplicación = a * b
    división = a // b
    return (suma, resta, multiplicación, división)

num1 = float ( input ("Ingrese el primer número:"))
num2 = float ( input ("Ingrese el segundo número:"))

resultados = operaciones_basicas (num1, num2)

print ("\nResultados:")
print ("El resultado de la suma es:", resultados [0])
print ("El resultado de la resta es:", resultados [1])
print ("El resultado de la multiplicación es:", resultados [2])
print ("El resultado de la división es:", resultados [3])

#Ejercicio 8

'''
Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales.
'''

def calular_imc (peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float (input ("Ingrese su peso en kilogramos:"))
altura = float (input ("Ingrese su altura en metros:"))

resultado = calular_imc (peso, altura)

print (f"Su índice de masa corporal (IMC) es:{resultado:.2f}")

#Ejercicio 9

'''
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función.
'''

def celsius_a_fahrenheit (celsius):
    pass
     
temperatura = float (input ("Ingrese la temperatura en Celsius:"))

resultado = celsius_a_fahrenheit (celsius)

#Ejercicio 10

'''
Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función.
'''

def calcular_promedio (a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = float (input ("Ingrese el primer número:"))
num2 = float (input ("Ingrese el segundo número:"))
num3 = float (input ("Ingrese el tercer número:"))

resultado = calcular_promedio (num1, num2, num3) 
print (f"El promedio entre estos tres números es: {resulado}")
