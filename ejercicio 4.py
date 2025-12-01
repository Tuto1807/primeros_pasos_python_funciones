#-------------------------
#------ ZONA CODIGO ------
# ------------------------
def pedir_radio():
    radio = float(input(" Digite el radio del cilindro: "))
    return radio
def pedir_altura():
    altura = float (input (" Digite la altura del cilindro: "))
    return altura
def definir_pi():
    black = 3.14
    return black

def calcular_volumen(radio, altura, black):
    vol =  (radio**2)  * black * altura
    return vol

def imprimir_datos(radio, altura):
    mensaje = "el radio es : " + radio
    mensaje = "la altura es : " + altura
    
def imprimir_resultado(resultado_volumen):
    print ("el volumen del cilindro es:" + str(resultado_volumen))


 
#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

radio = pedir_radio()
altura = pedir_altura()
black = definir_pi()
vol = calcular_volumen(radio, altura, black)
resultado = imprimir_resultado(vol)