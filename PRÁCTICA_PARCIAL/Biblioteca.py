títulos :list=["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
ejemplares :list=[5, 3, 7]
bandera :bool = True

while bandera:
    print ("Bienvenido a la biblioteca UTN")
    print ("Elija la opcion del menú que desea ejecutar")
    print ("1.Ingresar lista titulos")
    print ("2.Ingresar lista de ejemplares")
    print ("3.Mostrar catálogo")
    print ("4.Consultar disponibilidad de un título específico")
    print ("5.Listar disponibles")
    print ("6.Agregar título")
    print ("7.Ver títulos agotados")
    print ("8.Actualizar ejemplares (préstamo/devolución)")
    print ("9.Salir")
    opcion :str=input("Ingrese la opcion del menu que desea ejecutar: ")

    if opcion=="1":
        bandera_titulo :bool=True
        while bandera_titulo:
            titulo :str=input("Ingrese el titulo del libro: ")
            titulo=titulo.upper()
            while titulo=="":
             print("El titulo no puede estar vacio, ingrese de nuevo el titulo")
             titulo=input("Ingrese el titulo del libro: ")
             titulo=titulo.upper()
            titulos.append(titulo)
            desicion :str=input("Desea agregar otro titulo? S/N")
            if desicion.lower()=="n":
                 bandera_titulo=False