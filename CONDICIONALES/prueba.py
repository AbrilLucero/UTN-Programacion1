magnitud = float (input("Ingrese la magnitud del terremoto en la escala de Richter:"))

if magnitud <3:
    print ("Muy leve.")
elif magnitud >= 3 and magnitud < 4: 
    print ("Leve.")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte") 
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte")
else:
    print ("Extremo")