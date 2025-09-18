#Ejercicio 1
edad = int (input ("Ingrese su edad:"))

if edad > 18:
    print (f"Es mayor de edad")

#Ejercicio 2
nota = int (input ("Ingrese su nota:"))

if nota >= 6:
    print (f"Aprobado")
else:
    print (f"Desaprobado")

#Ejercicio 3
número = int ("Ingresar un número par:")

if número % 2 == 0:
    print (f"Ha ingresado un número par:")
else:
    print (f"Por favor, ingrese un número par:") 

#Ejercicio 4
edad = int (input ("Ingrese su edad:"))

if edad < 12:
    print (f"Categoría: Niño/a.")
elif edad >=12 and edad <18:
    print (f"Categoría: Adolescente.")
elif edad <=18 and edad <30:
    print (f"Categoría: Adulto/a joven.") 
else:
    print (f"Categoría: Adulto/a.")

#Ejercicio 5
contraseña = input ("Ingrese una contraseña de entre 8 y 14 caracteres:")
longitud = len (contraseña)

if longitud >= 8 and longitud <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres:")

#Ejercicio 6

import random
import statistics

numeros_aleatorios = [random.randint (1, 100) for i in range (50)]

moda = statistics.mode (numeros_aleatorios)
mediana = statistics.median (numeros_aleatorios)
media = statistics.mean (numeros_aleatorios)

print ("Lista de números aleatorios: {numeros_aleatorios}")
print ("Moda: {moda}")
print ("Mediana: {mediana}") 
print ("Media: {media}")

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
print ("Resultado:", texto)

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

magnitud = float (input ("Ingrese la magnitud del terremoto en la escala de Richter:"))

if magnitud < 3:
    clasificación = "Muy leve"
elif magnitud < 4: 
    clasificación = "Leve"
elif magnitud < 5:
    clasificación = "Moderado"
elif magnitud < 6:
    clasificación = "Fuerte"
elif magnitud < 7: 
    clasificación = "Muy fuerte"
else:
    clasificación = "Extremo"

print ("Clasificación:", clasificación)

#Ejercicio 10

def determinar_estacion():
    hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
    mes = input("¿Qué mes del año es? (ej. enero, febrero, etc.): ").lower()
    dia = int(input("¿Qué día del mes es?: "))

    estaciones_norte = {
        "invierno": (12, 21, 3, 20),
        "primavera": (3, 21, 6, 20),
        "verano": (6, 21, 9, 20),
        "otono": (9, 21, 12, 20)
    }

    estaciones_sur = {
        "verano": (12, 21, 3, 20),
        "otono": (3, 21, 6, 20),
        "invierno": (6, 21, 9, 20),
        "primavera": (9, 21, 12, 20)
    }

    meses_numeros = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }

    mes_num = meses_numeros.get(mes)

    if mes_num is None:
        print("Mes inválido.")
        return

    if hemisferio == "N":
        for estacion, (mes_inicio, dia_inicio, mes_fin, dia_fin) in estaciones_norte.items():
            if (mes_num == mes_inicio and dia >= dia_inicio) or \
               (mes_num == mes_fin and dia <= dia_fin) or \
               (mes_inicio < mes_num < mes_fin):
                print(f"En el hemisferio norte, es {estacion}.")
                return
    elif hemisferio == "S":
        for estacion, (mes_inicio, dia_inicio, mes_fin, dia_fin) in estaciones_sur.items():
            if (mes_num == mes_inicio and dia >= dia_inicio) or \
               (mes_num == mes_fin and dia <= dia_fin) or \
               (mes_inicio < mes_num < mes_fin):
                print(f"En el hemisferio sur, es {estacion}.")
                return
    else:
        print("Hemisferio inválido. Por favor, ingresa 'N' para Norte o 'S' para Sur.")
