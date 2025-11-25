#------------Zona Funcion------------
def capturar_num():
    numero = int(input("Escriba un numero"))
    return numero

def validar_num():
    dato_numero = 1
    while dato_numero != 0:
        dato_numero = capturar_num()
        if dato_numero%2==0:
            mensaje = "  par"
        else:
            mensaje = " impar"
        return mensaje
    
def imprimir_dato(dato_mensaje):
    print (" El numero es: "+ dato_mensaje)
    
def mensaje_alt():
    print ("Finalizo el programa.")
        
        
    
#------------Zona Codigo-------------

dato_mensaje = validar_num()
imprimir_dato(dato_mensaje)
mensaje_alt()
