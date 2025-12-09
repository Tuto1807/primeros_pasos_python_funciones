#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_kilometros():
    kilometros = float(input("Ingrese la distancia en kilómetros: "))
    return kilometros

def convertir_a_millas(kilometros):
    millas = kilometros * 0.621371
    return millas

def imprimir_datos(kilometros):
    print("La distancia en kilómetros es: " + str(kilometros))

def imprimir_resultado(millas):
    print("Equivale a " + str(millas) + " millas")



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

kilometros = solicitar_kilometros()
imprimir_datos(kilometros)
millas = convertir_a_millas(kilometros)
imprimir_resultado(millas)
