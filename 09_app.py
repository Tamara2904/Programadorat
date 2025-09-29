#Calculo monto a pagar para una factura (IGV - 18%)


#Definir el subtotal 

subtotal = float(input("Ingresa el subtotal: "))

# Definir el cáculo 
monto_igv = float(subtotal) * 0.18
monto_pagar = float(subtotal) + monto_igv

#Imprimir resultados
print(f"monto de subtotal: {subtotal}")
print(f"monto de IGV 18%: {monto_igv}")
print(f"monto total a pagar: {monto_pagar}")