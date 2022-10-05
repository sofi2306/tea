lista = []
while True:
    valor = input("Introducir número (o 'fin' para terminar): ")
    if valor.lower() in  "fin":
        break
    try:
        lista.append(int(valor))
    except ValueError:
        print ("Valor incorrecto, intente de nuevo. ")
    
print ("La suma de los numeros es: {}".format(sum(lista)))
print ("La cantidad es de {}".format(len(lista)))
print ("El promedio de valores es de {}".format(sum(lista)/len(lista)))
