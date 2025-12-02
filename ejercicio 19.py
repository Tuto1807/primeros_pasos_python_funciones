#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_longitud():
    long = float(input(" Digite la longitud del prisma triangular: "))
    return long
def pedir_ancho():
    ancho = float(input(" Digite el ancho del prisma triangular: "))
    return ancho
def pedir_altura():
    altura = float (input (" Digite la altura del prisma triangular: "))
    return altura
def calcular_area(long, ancho):
    area =  long * ancho  / 2
    return area

def calcular_vol(area, altura):
    vol = (area * altura)
    return vol

def imprimir_datos(long, ancho, altura):
    mensaje = "la longitud del prisma triangular es : " + long
    mensaje = "el ancho del prisma triangular es : " + ancho
    mensaje = "la altura del prisma triangular es  : " + altura

def imprimir_resultado1(resul_area):
    print ("el area del prisma triangular es:" + str(resul_area))


def imprimir_resultado2(resul_vol):
    print ("el volumen del prisma triangular es:" + str(resul_vol))


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
