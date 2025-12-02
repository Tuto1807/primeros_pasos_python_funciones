#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def definir_lado():
    lado = 8
    return lado

def calcular_volumen(lado):
    vol = lado ** 3
    return vol
def imprimir_datos(lado):
    mensaje = "la longitud del lado del cubo es: " + lado
    
def imprimir_mensaje (resultado):
    print ("El volumen del cubo es:" + str (resultado))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

lado = definir_lado()
vol = calcular_volumen(lado)
resultado = imprimir_mensaje(vol)