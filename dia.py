# --------- Zona Funcion ---------------
def capturar_nombre():
    nombre_usuario = input (" Escriba su nombre: ")
    return nombre_usuario
def capturar_hora():
    hora = int (input("escriba la hora " ))
    if hora >= 0 and hora < 12:
        print(" Buenos Dias ")
    elif hora >= 12 and hora < 18:
        print(" Buenas Tardes ")
    elif hora >= 18 and hora < 24 :
        print (" Buenas Noches ")
    else:
        print (" Hora incorrecta ")

def hacer_saludo(nombre_usuario):
    mensaje = " Hola " + nombre_usuario 
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#----------zona Codigo ---------------


nombre_usuario = capturar_nombre()
hora = capturar_hora()
mensaje = hacer_saludo(nombre_usuario) 
imprimir_mensaje(mensaje)