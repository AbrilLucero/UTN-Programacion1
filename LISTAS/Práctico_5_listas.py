#Ejercicio 1
numeros_multiplos_de_4 = list(range(0,101,4))
print ("Numeros del 1 al 100 que sean multiplos de 4:", numeros_multiplos_de_4) 

#Ejercicio 2
nombres = ["Hannah", "Abril", "Fernanda", "Faustina"]
print (nombres[-2])

#Ejercicio 3
lista_vacia = []
lista_vacia.append ("mariposa")
lista_vacia.append ("jardín")
lista_vacia.append ("trabajo")
print (lista_vacia)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[-3] = ("loro") #reemplazamos el segundo elemento
animales[-1] = ("oso") #reemplazamos el último elemento
print (animales)

#Ejercicio 5
numeros = [8, 15, 3, 22, 7] #se inicializa una lista 
numeros.remove (max(numeros)) #la función max encuentra el valor máximo dentro de la lista
print (numeros) #imprime la lista modificada sin el número máximo

#Ejercicio 6
numeros = list(range(10, 31, 5))
print("Los dos primeros numeros son:", numeros [0], numeros [1]) #imprime los dos primeros elementos

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos [-3] = ("focus") #reemplazamos el segundo elemento
autos [-2] = ("Nissan") #reemplazamos el último elemento
print(autos)

#Ejercicio 8
dobles = []
dobles.append (5*2)
dobles.append (10*2)
dobles.append (15*2)
print (dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append ("jugo") 
compras [1][1] = "tallarines"
compras [0].remove ("pan")
print (compras)

#Ejercicio 10
lista_anidada = []
lista_anidada.append (15)
lista_anidada.append (True)

sublista = []
sublista.append (25.5)
sublista.append (57.9)
sublista.append (30.6)

lista_anidada.append (sublista)
lista_anidada.append (False)
print (lista_anidada)


