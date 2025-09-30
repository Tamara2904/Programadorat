

# Problema Movi Express
# Solicitar al usuario la edad del pasajero 

edad = int(input("Ingrese la edad del pasajero: "))
 # Determinar la tarifa con if - elif - else 

if edad < 12: 
    tarifa = 3.00 
    tipo_tarifa = "Tarifa infantil"


elif edad <= 59:
    tarifa = 5.00 
    tipo_tarifa = "Tarifa regular"


else:
    tarifa = 2.00
    tipo_tarifa = "Tarifa Especial"

# Mostrar el mensaje final con un mensaje claro y formateado
print("--------------------------------")
print("Edad del pasajero:", edad)
print(tipo_tarifa + ": S/ ", tarifa)
print("--------------------------------")










