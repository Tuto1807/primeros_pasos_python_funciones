#-------------------------
#------ ZONA CODIGO ------
# ------------------------
import math
def pedir_num1():
    num1 = float (input("Digite numero que desea sacar raiz"))
    return num1

def calcular_numeros(num1):
    raiz = math.sqrt(num1)
    return raiz

def imprimir_resultado(raiz):
    print("La raiz del numero es: "+ str(raiz))


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

num1 = pedir_num1()
raiz = calcular_numeros(num1)
resultado = imprimir_resultado(raiz)
