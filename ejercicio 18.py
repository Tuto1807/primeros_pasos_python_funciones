#-------------------------
#------ ZONA CODIGO ------
# ------------------------
import math
def definir_lado():
    lado = 8
    return lado
def calcular_area(lado):
    area = (3 * math.sqrt(3) / 2) * lado**2
    return area
def imprimir_datos(lado):
    mensaje = "la longitud del lado del hexagono es: " + lado
    
def imprimir_mensaje (resultado):
    print ("El resultado del area del hexagono es:" + str (resultado))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

lado = definir_lado()
area = calcular_area(lado)
resultado = imprimir_mensaje(area)