#------------Zona Funcion------------
def dar_letra():
    while True:
     print("Digite la letra 'A' para Actualizar Sistema ")
     print("Digite la letra 'B' para Eliminar Catalogo ")
     print("Digite la letra 'C' para Crear Productos ")
     print("Digite la letra 'D' para Salir del Programa ")
     letra = str (input (" seleccione opcion "))   
     return letra
 
def validar_letra(dato_let):
    
     if dato_let=='D' or dato_let== 'd':
        mensaje = "Finalizando con Exito. "
     elif dato_let == 'A' or dato_let == 'a':
        mensaje = "Actualizando Sistema........"
    
     elif dato_let =='B' or dato_let =='b':
         mensaje = "Eliminando Catalogo.........."
     elif dato_let =='C' or dato_let=='c':
        mensaje = "Creando productos........"
        
     return mensaje
        
def dar_mensaje(dato_mensaje):
    print("Se está " + dato_mensaje)
    
def mensaje_alt():
    print("El DO-WHILE ha finalizado.")    

        
#------------Zona Codigo-------------

dato_let = dar_letra()
dato_mensaje= validar_letra(dato_let)
dar_mensaje (dato_mensaje)
mensaje_alt()
