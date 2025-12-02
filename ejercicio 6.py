#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_radio():
    radio = float(input ("Digite el radio del Cono: "))
    return radio

def pedir_altura():
    altura = float(input ("Digite la altura del Cono: "))
    return altura

def definir_pi():
    black = float (3.14)
    return black

def calcular_volu(radio, altura, black):
    vol = 0.33 * black * (radio**2) * altura
    return vol

def imprimir_datos(radio, altura):
    mensaje = "El radio del cono es: " + radio
    mensaje = "La altura del cono es: " + altura

def imprimir_resultado(resul_vol):
    print ("El volumen del cono es: " + str (resul_vol))

#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

radio = pedir_radio()
altura = pedir_altura()
vol = calcular_volu(radio, altura, black=3.14)
resultado = imprimir_resultado(vol)

