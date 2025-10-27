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