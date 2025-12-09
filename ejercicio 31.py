#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_horas():
    horas = float(input("Ingrese el número de horas: "))
    return horas

def convertir_a_minutos(horas):
    minutos = horas * 60
    return minutos

def imprimir_datos(horas):
    print("Las horas ingresadas son: " + str(horas))

def imprimir_resultado(minutos):
    print("Equivalen a " + str(minutos) + " minutos")



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

horas = solicitar_horas()
imprimir_datos(horas)
minutos = convertir_a_minutos(horas)
imprimir_resultado(minutos)
