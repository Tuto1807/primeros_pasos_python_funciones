#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def definir_celsius():
    celsius = float(input("Digite cuantos grados desea convertir: "))
    return celsius

def calcular_faren(celsius):
    faren = celsius * 9/5 + 32
    return faren

def imprimir_datos (celsius):
    mensaje = "Los grados celsius son: "

def imprimir_resultado(resultado_faren):
    print ("La conversion a grados Fahrenheit dio = "+ str (resultado_faren) )


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

celsius = definir_celsius()
faren = calcular_faren(celsius)
resultado = imprimir_resultado(faren)

