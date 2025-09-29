#Conversiones de tipo de datos

#int()-> conviernte a número entero
#Sirve para convertir un valor a número entero(int)
#Si el valor es un número decimal, corta la parte decimal (no redondea)
#Si el valor es un texto que representa un número entero, también funciona.

int("25") #(cadena de entero)
int(3.9)  #(decimal a entero, elimina los decimales)
int(True) #(True equivale a 1)
int(False)#(False equivale a 0)


# float() -> Covierte a número decimal 
# Convierte valores a número decimal (float).
# Muy útil para operaciones matemáticas donde necesitas decimales.
float("3.14") #(cadena a decimal)
float(10)     #(entero a decimal)
float(True)   # 1.0
float(False)  # 0.0


str()->Convierte a cadena de texto
#concierte cualquier tipo de dato a texto (str)
#útil para mostrar mensajes al usuario o para concater textos.
srt(100)            #(entero a cadena)
srt(3.14)           #"3.14"
srt(True)           #"True"
srt([1, 2, 3])      #"[1, 2, 3]"

#bool()-> Convierte a valor lógico (True o False)
#Convierte valores a booleano (True o False)
bool(0)        #False
bool(1)        #True
bool("")       #False(cadena vacía)
bool("hola")   #True(cadena con contenido)
bool([])       #False(lista vacia)
bool([1,2])    #True(lista con elementos)



