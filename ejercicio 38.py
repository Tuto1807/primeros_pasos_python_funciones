#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_primer_numero():
    numero1 = float(input("Ingrese el primer número: "))
    return numero1

def solicitar_segundo_numero():
    numero2 = float(input("Ingrese el segundo número: "))
    return numero2

def determinar_mayor(numero1, numero2):
    if numero1 > numero2:
        mayor = numero1
    else:
        mayor = numero2
    return mayor

def imprimir_datos(numero1, numero2):
    print("El primer número es: " + str(numero1))
    print("El segundo número es: " + str(numero2))

def imprimir_resultado(mayor):
    print("El número mayor es: " + str(mayor))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

numero1 = solicitar_primer_numero()
numero2 = solicitar_segundo_numero()
imprimir_datos(numero1, numero2)
mayor = determinar_mayor(numero1, numero2)
imprimir_resultado(mayor)
