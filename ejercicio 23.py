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
    mult = num1 * num2
    return mult

def imprimir_resultado(mult):
    print("La multiplicacion de los 2 numeros es: "+ str(mult))


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

num1 = pedir_num1()
num2 = pedir_num2()
mult = calcular_numeros(num1, num2)
resultado = imprimir_resultado(mult)
