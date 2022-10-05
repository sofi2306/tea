def calcularSalario(horas, tarifa):
    horas_extras = horas - MAX_HORAS_SEMALALES
    if (horas_extras > 0):
        pago = (MAX_HORAS_SEMALALES * tarifa) + (horas_extras * (tarifa * 1.5))
    else:
        pago = horas * tarifa
    return pago

try:
    MAX_HORAS_SEMALALES = 40
    horas = int(input("Ingrese el número de horas: "))
    tarifa = float(input("Ingrese la tarifa por horas: "))
    salario = calcularSalario(horas, tarifa)
    print (salario)
except:
    print("Error, debe ingresar un valor numérico")