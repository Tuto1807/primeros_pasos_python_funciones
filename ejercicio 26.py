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
    residuo = num1 % num2
    return residuo

def imprimir_resultado(residuo):
    print("el residuo de la division de los 2 numeros es: "+ str(residuo))


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

num1 = pedir_num1()
num2 = pedir_num2()
residuo = calcular_numeros(num1, num2)
resultado = imprimir_resultado(residuo)
