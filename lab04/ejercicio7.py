def calculaCalificacion (grado):
    if (puntuacion >0.9 and puntuacion <=1):
        grado = "Sobresaliente"
    elif (puntuacion >0.8 and puntuacion <=0.9):
        grado = "Notable"
    elif (puntuacion >0.7 and puntuacion <=0.8):
        grado = "Bien"
    elif (puntuacion >=0.6 and puntuacion <=0.7):
        grado = "Sufuciente"
    elif (puntuacion >0 and puntuacion <0.6):
        grado = "Insuficiente"
    else:
        grado = "Puntuación incorrecta"
    return grado  

try:
    puntuacion = float(input("Introduzca puntuación: "))
    grado = calculaCalificacion(puntuacion)
    print ("Su calificación es: ", grado)

except:
    print("Puntuación incorrecta")