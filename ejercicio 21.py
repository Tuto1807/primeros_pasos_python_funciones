#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_num1():
    num1 = float (input("Digite primer numero"))
    return num1

def pedir_num2():
    num2 = float (input ("Digite segundo numero"))
    return num2

def calcular_numeros(num1, num2):
    suma = num1 + num2
    return suma

def imprimir_resultado(suma):
    print("La suma de los 2 numeros es: "+ int(suma))


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

num1 = pedir_num1()
num2 = pedir_num2()
suma = calcular_numeros(num1, num2)
resultado = imprimir_resultado(suma)
