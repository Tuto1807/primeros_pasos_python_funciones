#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_primer_numero():
    numero1 = float(input("Ingrese el primer número: "))
    return numero1

def solicitar_segundo_numero():
    numero2 = float(input("Ingrese el segundo número: "))
    return numero2

def calcular_promedio(numero1, numero2):
    promedio = (numero1 + numero2) / 2
    return promedio

def imprimir_datos(numero1, numero2):
    print("El primer número es: " + str(numero1))
    print("El segundo número es: " + str(numero2))

def imprimir_resultado(promedio):
    print("El promedio de ambos números es: " + str(promedio))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

numero1 = solicitar_primer_numero()
numero2 = solicitar_segundo_numero()
imprimir_datos(numero1, numero2)
promedio = calcular_promedio(numero1, numero2)
imprimir_resultado(promedio)
