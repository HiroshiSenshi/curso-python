#print -> imprime en consola
# Comentarios de una sola línea
"""
Comentarios
Multilinea
"""
print("Hola mundo")

# Variables
# Son contenedores que almacenan un dato, valor, etc.

#Formas de declarar variables

myvar = "Gato 1"
my_var = "Gato 2"
_my_var = "Gato 3"
myVar = "Gato 4"
MYVAR = "Gato 5"
myvar2 = "Gato 6"

myVariableName = "Gato 7"  #Camel Case
MyVariableName = "Gato 8"  #Pascal Case
my_variable_name = "Gato 9" #Snake Case

#Formas incorrectas de declarar variables
"""
15myvar = "Gato 10"
my-var = "Gato 11"
my var = "Gato 12"
"""

# Case-sensitive: distingue entre mayúsculas y minúsculas
a = "Gato 13"
A = 'Gato 14'

#Crear 1 variable que almacene un número entero, 1 variable que almacene un flotante y 3 variables que almacenen un string

my_variable_name = 10
MyVariableNum = -3.5
my_var = "zoo"
myvar2 = "elefante"
myvar = "25.45"

#Mi variable de tipo entrero es: valor
print("Mi variable de tipo entero es: ", my_variable_name)
print("Mi variable de tipo flotante es: ", MyVariableNum)
print("Mi variable de tipo entero es: " + my_var)

#Cambiar el tipo de variable entero y flotante a string
#Cambiar el tipo de variable string a entero

# 1° -> Casting
print("**Casting**")
print("Cambio de variable de entero a string: " + str(my_variable_name))
#print("Cambio de variable de entero a string: " + my_variable_name)

# 2° --> Re-asignación

my_variable_name = str(my_variable_name)
print("Cambio de variable de entero a string: " + my_variable_name)

print("Cambio de variable de tipo string a entero: \n", float(myvar)) #int

print("El tipo de la variable myvar es: ", type(myvar))

#Aignar múltiples valores a múltiples variables
"""
Imprimir:
El color 1 es: suvalor
El color 2 es: suvalor
El color 3 es: suvalor
"""
color1, color2, color3 = "Rojo", "Verde", "Morado"
#print("El color uno es: ", "color1\n" "El color dos es :","color2\n""El color 3 es: ", "color3\n" ) #Sara
print("El color uno es: ", color1, "\nEl color dos es: ", color2, "\nEl color 3 es: ", color3 ) #Sara Corregido
#print("El color uno es:,\n,"El color 2 es:" ,\n , "El color 3 es: : ,"\n") #Hiro
#print("El color uno es: "color 1\n" "El color dos es:" "color 2\n" "El color tres es:" "color 3\n") #Rodrigo

# Asignar un mismo valor a múltiples variables

torta = "Pastor"
torta2 = torta

taco1 = taco2 = taco3 = "Suadero"
print(taco1, taco2, taco3)
#taco1 = "Suadero"
#taco2 = "Suadero"
#taco3 = "Suadero"

#Booleanos

true_var = True
false_var = False

print("La variable true_var es: ", true_var)

name = "Paco"
apellido = "Gonzalez"
#Paco Gonzalez
nombre_completo = name + " " + apellido#Sara
#nombre_completo = name +  apellido     #Hiro
#nombre_completo = name + apellido   #Ro

print(nombre_completo)

number1 = 5
number2 = 6

total = str(number1) + str(number2)
print(total)
#56
#11

#¿Cuáles son los operadores aritméticos de Python? 
#¿Cuáles son los operadores de asignación de Python?
#Traer un ejemplo de cada uno

#Operador de adición --> +
print(2+10)
