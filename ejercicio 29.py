#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_numero():
    numero = int(input("Ingrese un número: "))
    return numero

def determinar_par_impar(numero):
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return resultado

def imprimir_resultado(numero, resultado):
    print("El número " + str(numero) + " es " + resultado)



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

numero = solicitar_numero()
resultado = determinar_par_impar(numero)
imprimir_resultado(numero, resultado)
