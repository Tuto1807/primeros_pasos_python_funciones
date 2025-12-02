#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_longitud():
    long = float(input(" Digite la longitud de la piramide: "))
    return long
def pedir_ancho():
    ancho = float(input(" Digite el ancho de la piramide: "))
    return ancho
def pedir_altura():
    altura = float (input (" Digite la altura de la piramide: "))
    return altura
def calcular_area(long, ancho):
    area =  long * ancho  / 2
    return area

def calcular_vol(area, altura):
    vol = (area * altura) / 3
    return vol

def imprimir_datos(long, ancho, altura):
    mensaje = "la longitud de la piramide es : " + long
    mensaje = "el ancho de la piramide es : " + ancho
    mensaje = "la altura de la piramide es  : " + altura
    
def imprimir_resultado1(resul_area):
    print ("el area de la piramide es:" + str(resul_area))


def imprimir_resultado2(resul_vol):
    print ("el volumen de la piramide es:" + str(resul_vol))


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------


long = pedir_longitud()
ancho = pedir_ancho()
altura = pedir_altura()
area = calcular_area(long, ancho)
vol = calcular_vol(area, altura)
resultado1 = imprimir_resultado1(area)
resultado2 = imprimir_resultado2(vol)
