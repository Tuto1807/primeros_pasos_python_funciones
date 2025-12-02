#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_longitud():
    long = float(input(" Digite la longitud del prisma rectangular: "))
    return long
def pedir_ancho():
    ancho = float(input(" Digite el ancho del prisma rectangular: "))
    return ancho
def pedir_altura():
    altura = float (input (" Digite la altura del prisma rectangular: "))
    return altura
def calcular_volumen(long, ancho, altura):
    vol =  long * ancho * altura
    return vol

def imprimir_datos(long, ancho, altura):
    mensaje = "la longitud del prisma es : " + long
    mensaje = "el ancho del prisma es : " + ancho
    mensaje = "la altura del prisma es  : " + altura
    
def imprimir_resultado(resul_vol):
    print ("el volumen del prisma es" + str(resul_vol))





#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

long = pedir_longitud()
ancho = pedir_ancho()
altura = pedir_altura()
vol = calcular_volumen(long, ancho, altura)
resultado = imprimir_resultado(vol)