def determinar_estacion():
    hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
    mes = input("¿Qué mes del año es? (ej. enero, febrero, etc.): ").lower()
    dia = int(input("¿Qué día del mes es?: "))

    estaciones_norte = {
        "invierno": (12, 21, 3, 20),
        "primavera": (3, 21, 6, 20),
        "verano": (6, 21, 9, 20),
        "otono": (9, 21, 12, 20)}

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
