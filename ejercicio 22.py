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
    rest = num1 - num2
    return rest

def imprimir_resultado(rest):
    print("La resta de los 2 numeros es: "+ str(rest))


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

num1 = pedir_num1()
num2 = pedir_num2()
rest = calcular_numeros(num1, num2)
resultado = imprimir_resultado(rest)
