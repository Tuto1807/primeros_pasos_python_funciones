#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_num1():
    num1 = float (input("Digite numero que desea calcular: "))
    return num1

def calcular_numero(num1):
    cuadrado = num1 ** 2
    return cuadrado

def imprimir_resultado(cuadrado):
    print(f"el cuadrado de {num1} es: {cuadrado}")

#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

num1 = pedir_num1()
cuadrado = calcular_numero(num1)
resultado = imprimir_resultado(cuadrado)
