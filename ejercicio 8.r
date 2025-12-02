#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_dolares():
    dolares = float(input("Digite cantidad de dolares que desea convertir: "))
    return dolares

def definir_tasa():
    tasa_cambio = 0.85
    return tasa_cambio

def convertir_dolares_euros(dolares, tasa_cambio):
    euros = dolares * tasa_cambio
    return euros


def imprimir_resultado(resultado_euros):
    print (f"{dolares} dolares equivalen a {euros} euros  con una tasa de cambio de {tasa_cambio}.")






#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

dolares = pedir_dolares()
tasa_cambio = definir_tasa()
euros = convertir_dolares_euros(dolares, tasa_cambio)
resultado = imprimir_resultado(euros)

