#Examen 1 introducción a la programación 

# Problema 1 Global Change
# Solicitar al usuario el monto en soles (PEN) que desea cambiar.


monto_en_soles = float(input("Ingrese el monto en soles (PEN): "))

# Preguntar la tasa de cambio actual (por ejemplo, 1 USD = 3.85 PEN).


tasa_de_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = ? PEN): "))

# Calcular y mostrar el equivalente en dólares (USD).

monto_en_dolares = monto_en_soles / tasa_de_cambio

# Mostrar el resultado con dos decimales, indicando claramente el monto ingresado y el monto convertido.
print("---Conversión en Global Change---")
print("Usted ingresó:", "S/", monto_en_soles, "soles")
print(f"El equivalente en dólares es: $ {monto_en_dolares:.2f} USD")











