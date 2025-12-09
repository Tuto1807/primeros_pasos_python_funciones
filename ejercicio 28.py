#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_altura():
    altura = float(input("Ingrese la altura del triángulo: "))
    return altura

def solicitar_base():
    base = float(input("Ingrese la base del triángulo: "))
    return base

def calcular_area(base, altura):
    area = (base * altura) / 2
    return area

def imprimir_datos(base, altura):
    print("La base es: " + str(base))
    print("La altura es: " + str(altura))
    
def imprimir_resultado(resultado_area):
    print("El área del triángulo es: " + str(resultado_area))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

base = solicitar_base()
altura = solicitar_altura()
imprimir_datos(base, altura)
area = calcular_area(base, altura)
imprimir_resultado(area)
