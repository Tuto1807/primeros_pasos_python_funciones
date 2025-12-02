#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_litros():
    lt = float (input(" Digite cantidad de litros que desea convertir:  "))
    return lt

def convertir_lt_galon(lt):
    galon = lt / 3.785
    return galon

def imprimir_datos(lt):
    mensaje = "Los litros que deseas convertir son: " + lt

def imprimir_resul(lt, galon):
    print (f"{lt} litros  equivalen a {galon} galones")


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

lt = pedir_litros()
galon = convertir_lt_galon(lt)
resultado = imprimir_resul(lt, galon)