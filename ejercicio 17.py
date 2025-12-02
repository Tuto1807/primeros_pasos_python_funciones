#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_libras():
    lb = float (input(" Digite cantidad de libras que desea convertir:"))
    return lb

def convertir_libras_kg(lb):
    kg = lb /  2.205
    return kg

def imprimir_datos(lb):
    mensaje = "Las libras que deseas convertir son: " + lb


def imprimir_resul(lb, kg):
    print (f"{lb} libra  equivalen a {kg} kilos")


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

lb = pedir_libras()
kg = convertir_libras_kg(lb)
resultado = imprimir_resul(lb, kg)
