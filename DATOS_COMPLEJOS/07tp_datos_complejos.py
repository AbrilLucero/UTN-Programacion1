#Ejercicio 1

'''
Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300
'''

precios_frutas = {'Banana' : 1200, 'Ananá' : 2500, 'Melón' : 3000, 'Uva' : 1450}

precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

print (precios_frutas)

#Ejercicio 2

''''
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800 
'''

precios_frutas = {'Banana' : 1200, 'Ananá' : 2500, 'Melón' : 3000, 'Uva' : 1450}

precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800

print (precios_frutas)

#Ejercicio 3

'''
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios. 
'''
precios_frutas = {'Banana' : 1200, 'Ananá' : 2500, 'Melón' : 3000, 'Uva' : 1450}
lista_frutas = list(precios_frutas.keys())
print (lista_frutas)

#Ejercicio 4
'''
Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. 
Ejemplo: 

'''
contactos = {}
print ("-- Cargar 5 Contactos --")

for i in range (5):
    nombre = input (f"Ingresa el nombre del contacto {i+1}:").strip()
    número = input (f"Ingresa el número de teléfono de {nombre}:").strip()

contactos [nombre] = número
print("-" * 30)

print("¡Carga completa! Agenda de contactos actual:")
print(contactos)

print ("-------Consulta de contactos-------")
nombre_a_buscar = input("Ingresa el nombre del contacto que deseas buscar: ").strip()
numero_encontrado = contactos.get(nombre_a_buscar)
if numero_encontrado:
    print(f"El número de teléfono de *{nombre_a_buscar}* es: *{numero_encontrado}*")
else:
    print(f"Lo siento, el contacto '{nombre_a_buscar}' no se encuentra en la agenda.")
    
#Ejercicio 5

#solicitamos la frase al usuario
frase:str = input ("Ingrese una frase:")
c = {frase}
print (c)

#convertir las palabras en minúsculas y las separamos
palabras = frase.lower().split()

#creamos un conjunto con las palabras únicas
palabras_unicas = set(palabras)

#crear un diccionario
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Palabras_únicas:", palabras_unicas)
print("Recuento:", recuento)


#Ejercicio 6

# Creamos un diccionario para guardar los alumnos y sus notas
alumnos = {}

# Pedimos datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    
    # Ingresamos tres notas separadas por espacio y lo convertimos a tupla
    notas = input(f"Ingresá las 3 notas de {nombre} separadas por espacio: ")
    notas = tuple(map(float, notas.split()))  
    
    alumnos[nombre] = notas

# Mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

#Ejercicio 7

# Ipermitimos ingresar los alumnos que aprobaron cada parcial
parcial1 = set(input("Ingresá los nombres de quienes aprobaron el Parcial 1, separados por espacio: ").split())
parcial2 = set(input("Ingresá los nombres de quienes aprobaron el Parcial 2, separados por espacio: ").split())

# Los que aprobaron ambos parciales , utilizamos intersección
ambos = parcial1 & parcial2

# Los que aprobaron solo uno , utilizamos diferencia simétrica
solo_uno = parcial1 ^ parcial2

# Los que aprobaron al menos uno , utilizamos unión
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("\nAprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

#Ejercicio 8

#creamos el diccionario con productos y su stock
productos = {"Aceite": 700, "Mayonesa": 3600, "Queso": 1200, "Yerba": 8000}

#consultamos el stock de un producto
opción = 0
print (f"El stock de los productos es el siguiente: {productos}")
while opción != 4:
    print ("1: Consultar stock de un producto")
    print ("2: Agregar unidades al stock de un producto")
    print ("3: Agregar un nuevo producto")
    print ("4: Salir")
    opción = int (input ("Seleccione opción:"))

    if opción == 1:
        nombre_producto = input ("Ingrese el nombre del producto:")
        if nombre_producto in productos :
            print (f"El producto {nombre_producto} tiene un stock de {productos[nombre_producto]} ")
        else:
            print ("No existe el producto ingresado.")

    if opción == 2:
        nombre_producto = input ("Ingrese el nombre del producto que desea modificar su stock:")
        if nombre_producto in productos:
            nueva_cantidad = int (input ("Ingrese el nuevo stock para este producto:"))
            productos [nombre_producto]= nueva_cantidad
            
            



#Ejercicio 9

'''
Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
Ejemplo: 
Permití consultar qué actividad hay en cierto día y hora. 
'''

#Ejercicio 10

'''
Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores. 
'''