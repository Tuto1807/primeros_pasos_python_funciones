#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def definir_radio():
    radio = 8
    return radio

def calcular_volumen(radio):
    vol =  ( 4 * 3.14 * 8)
    return vol
def imprimir_datos(radio):
    mensaje = "el radio es: " + radio
    
def imprimir_mensaje (resultado):
    print ("El volumen de la esfera es:" + str (resultado))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

radio = definir_radio()
vol = calcular_volumen(radio)
resultado = imprimir_mensaje(vol)
