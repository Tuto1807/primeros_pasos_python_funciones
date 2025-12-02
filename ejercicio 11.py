#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_km():
    km = float (input(" Digite cantidad de kilometros que desea convertir:  "))
    return km

def convertir_km_millas(km):
    millas = km * 0.621
    return millas

def imprimir_datos(km):
    mensaje = "Los kilometros que deseas convertir son: " + km

def imprimir_resul(km, millas):
    print (f"{km} kilometros  equivalen a {millas} millas")


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

km = pedir_km()
millas = convertir_km_millas(km)
resultado = imprimir_resul(km, millas)