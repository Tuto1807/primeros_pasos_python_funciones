#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_cantidad():
    cantidad = float(input("Ingrese la cantidad de dinero en la cuenta: "))
    return cantidad

def calcular_interes(cantidad):
    interes = cantidad * 0.05
    return interes

def calcular_total(cantidad, interes):
    total = cantidad + interes
    return total

def imprimir_datos(cantidad):
    print("La cantidad inicial es: " + str(cantidad))

def imprimir_resultado(interes, total):
    print("El interés del 5% es: " + str(interes))
    print("El total con interés es: " + str(total))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

cantidad = solicitar_cantidad()
imprimir_datos(cantidad)
interes = calcular_interes(cantidad)
total = calcular_total(cantidad, interes)
imprimir_resultado(interes, total)
