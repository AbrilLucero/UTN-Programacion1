especialidades :list= ["Dermatología", "Cardiología", "Endocrinología", "Pediatría"]
cupos :list= [4, 5, 7, 3]
bandera :bool = True

while bandera: 
    print ("--BIENVENIDO A LA CLÍNICA--")
    print ("Elija la opción que desea ejecutar")
    print ("1-Ingresar lista de especialidades")
    print ("2-Ingresar lista de cupos disponibles")
    print ("3-Mostrar agenda")
    print ("4-Consultar disponibilidad de cupos de una especialidad")
    print ("5-Listar especialidades sin cupo")
    print ("6-Agregar especialidad")
    print ("7-Mostrar las especialidades sin disponibilidad")
    print ("8- Actualizar cupos (reservar/cancelar)")
    print ("9- Mostrar la agenda")
    print ("10- Salir")
    opcion :str=input("Ingrese la opcion que desea ejecutar: ")

    if opcion == "1":
        bandera_especialidades :bool=True
        while bandera_especialidades:
            especialidades :str=input ("Ingrese el nombre de la especialidad:")
            especialidades=especialidades.upper ()
            while especialidades=="":
                print ("El nombre no puede estar vacío, por favor ingrese de nuevo el nombre:") #si el usuario ingresa un nombre vacío
                especialidades=input("Ingrese el nombre de la especialidad: ")
                especialidades=especialidades.upper()
                especialidades.append(especialidades)
        desicion :str=input("Desea agregar otra especialidad? S/N")
        if desicion.lower()=="n":
            bandera_especialidades=False

    elif opcion == "2":
        for i in range (len (especialidades)):
            print (f"La especialidad tiene: {cupos[i]} cupos")
            cupos_especialidades :str=input ("Ingrese el numero de cupos disponibles")
            while cupos_especialidades.ishapha () or int (cupos_especialidades) <0:
                print ("No es válido")
            cupos_especialidades= input("Ingrese el numero de cupos disponibles para esta especialidad:")
        cupos_disponibles.append (int(cupos_especialidades)) 
        print (f"La especialidad {especialidades[i]} tiene {cupos_especialidades[i]} disponibles")