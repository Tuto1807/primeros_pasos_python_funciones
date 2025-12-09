#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_radio():
    radio = float(input("Ingrese el radio del círculo: "))
    return radio

def calcular_circunferencia(radio):
    pi = 3.1416
    circunferencia = 2 * pi * radio
    return circunferencia

def imprimir_datos(radio):
    print("El radio es: " + str(radio))

def imprimir_resultado(resultado_circunferencia):
    print("La circunferencia del círculo es: " + str(resultado_circunferencia))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

radio = solicitar_radio()
imprimir_datos(radio)
circunferencia = calcular_circunferencia(radio)
imprimir_resultado(circunferencia)
