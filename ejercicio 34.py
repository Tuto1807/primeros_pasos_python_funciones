#-------------------------
#------ ZONA CODIGO ------
#-------------------------

def solicitar_precio():
    precio = float(input("Ingrese el precio del artículo: "))
    return precio

def calcular_descuento(precio):
    descuento = precio * 0.10
    return descuento

def calcular_precio_final(precio, descuento):
    precio_final = precio - descuento
    return precio_final

def imprimir_datos(precio):
    print("El precio original es: " + str(precio))

def imprimir_resultado(descuento, precio_final):
    print("El descuento del 10% es: " + str(descuento))
    print("El precio final es: " + str(precio_final))



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

precio = solicitar_precio()
imprimir_datos(precio)
descuento = calcular_descuento(precio)
precio_final = calcular_precio_final(precio, descuento)
imprimir_resultado(descuento, precio_final)
