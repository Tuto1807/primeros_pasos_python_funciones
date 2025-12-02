#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_base():
    Base = float(input(" Digite la base mayor del trapecio: "))
    return Base
def pedir_base_menor():
    base = float(input(" Digite la base menor del trapecio: "))
    return base
def pedir_altura():
    altura = float (input (" Digite la altura del trapecio: "))
    return altura
def calcular_area(Base, base, altura):
    area = (Base + base)/2 * altura
    return area

def imprimir_datos(Base, base, altura):
    mensaje = "La base mayor del trapecio es : " + Base
    mensaje = "La base menor del trapecio es : " + base
    mensaje = "la altura del trapecio es : " + altura
    
def imprimir_resultado(resultado_area):
    print ("el resultado del area es:" + str(resultado_area))






#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

Base =  pedir_base()
base = pedir_base_menor()
altura = pedir_altura()
area = calcular_area(Base, base, altura)
resultado = imprimir_resultado(area)
