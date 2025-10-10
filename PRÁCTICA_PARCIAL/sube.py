tarjetas :list = [1234567890123456, 9876543210987654, 5555666677778888]
saldos :list = [150.50, 25.00, -10.00]
bandera :bool= True

while bandera:
    print ("--BIENVENIDO AL SISTEMA SUBE--")
    print ("")
    print ("1.Ingresar numeros de tarjetas:")
    print ("2. Ingresar saldos correspondientes:")
    print ("3. Mostrar tarjetas y saldos:")
    print ("4. Consultar saldo de la tarjeta:")
    print ("5. Listar saldos en negativo o cero:")
    print ("6.Agregar tarjeta:")
    print ("7. Ver saldos negativos o cero")
    print ("8. Cargar/debitar saldo")
    print ("9.Salir")
    opcion :str=input ("Ingrese la opcion que desea ejecutar:")

    if opcion == "1":
        bandera_tarjetas :bool=True
        while bandera_tarjetas:
            tarjetas int(input("Ingrese el número de la tarjeta: "))
            tarjetas=tarjetas.upper()
            tarjetas.append (tarjetas)
        print (f"el numero de la tarjeta {tarjetas} es:")
            