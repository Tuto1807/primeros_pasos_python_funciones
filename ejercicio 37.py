#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_primer_numero():
    numero1 = int(input("Ingrese el primer número: "))
    return numero1

def solicitar_segundo_numero():
    numero2 = int(input("Ingrese el segundo número: "))
    return numero2

def verificar_multiplo(numero1, numero2):
    if numero1 % numero2 == 0:
        resultado = "es múltiplo"
    else:
        resultado = "no es múltiplo"
    return resultado

def imprimir_datos(numero1, numero2):
    print("El primer número es: " + str(numero1))
    print("El segundo número es: " + str(numero2))

def imprimir_resultado(numero1, numero2, resultado):
    print(str(numero1) + " " + resultado + " de " + str(numero2))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

numero1 = solicitar_primer_numero()
numero2 = solicitar_segundo_numero()
imprimir_datos(numero1, numero2)
resultado = verificar_multiplo(numero1, numero2)
imprimir_resultado(numero1, numero2, resultado)
