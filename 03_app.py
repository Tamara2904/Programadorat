# Variables 
#Las variables son palabras específicas que utilizamos para asignar y almacenar valores específicos que podemos recuperar en cualquier momento.


# Variable nombre 
nombre ="Tamara"
telefono=926432538
name="tamara"
#Visualizando el contenido de las variables

print(nombre)
print(telefono)
print(name)
#Jugando con variables 
age=30

print(age)
print(f"Edad:{age}")

distric="San Luis"
print(distric)
print(f"Distrito:{distric}")
print(f"Nomre de distrito:{distric}")

# Precio del producto
price = 90
print(price)
print(f"El precio de costo es:{price}")
# Es un cliente activo
is_active_client=True
print(is_active_client)
print(f"¿Esta activo?{is_active_client}")

is_active_client=False
print(is_active_client)
print(f"¿Esta activo?{is_active_client}")

#Trabajando con fechas

from datetime import date 
fecha_clase = date(2025, 9, 22) #(yyyy, mm, dd)
print(fecha_clase)
print(f"la fecha de hoy es : {fecha_clase}")

fecha_formateada = fecha_clase.strftime("%d/%m/%Y")
print(f"La fecha con formato es: {fecha_formateada}")