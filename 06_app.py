#Averiguando los tipos de datos de las variables

#Variable de tipo cadena de texto
dispositivo = "Computador"
print(dispositivo)
print(type(dispositivo))

#Variable de tipo entero 
cantidad=45
print(cantidad)
print(type(cantidad))

#Variable de tipo decimal / flotante
precio=14.99
print(precio)
print(type(precio))

#Tipo de dato boleano
is_active_client = True
print(is_active_client)
print(type(is_active_client))

#Tipo de dato fecha

from datetime import date
fecha_cumple = date(2025, 9, 18)
print(fecha_cumple)
print(f"Fecha de cumpleaños: {fecha_cumple}")
fecha_formateada = fecha_cumple.strftime("%d/%m%Y")
print(f"la fecha formateada es: {fecha_formateada}")
print(type(fecha_cumple))


#Clase terminada 

