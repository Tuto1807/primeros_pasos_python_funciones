#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_longitud():
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    return longitud

def solicitar_ancho():
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    return ancho

def calcular_area(longitud, ancho):
    area = longitud * ancho
    return area

def imprimir_datos(longitud, ancho):
    print("La longitud es: " + str(longitud))
    print("El ancho es: " + str(ancho))

def imprimir_resultado(resultado_area):
    print("El área del rectángulo es: " + str(resultado_area))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

longitud = solicitar_longitud()
ancho = solicitar_ancho()
imprimir_datos(longitud, ancho)
area = calcular_area(longitud, ancho)
imprimir_resultado(area)
