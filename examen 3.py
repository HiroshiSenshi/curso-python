
#Quitar espacios 
print("     El arbol caido del cielo    ".strip())

#Intercambiar entre mayuscula y minuscula
print('La CoMiDa dEl Cui'.lower())
print('La CoMiDa dEl Cui'.casefold())

#Verifica las palabras 

Checadoneitor = 'cerveza','jack daniels','micheladotas','pizza','perro'
x = 9
try:
    print(x)
    
except NameError:
    print("No está la palabra :cui")
else:
    print("La excepción no fue valuerror")

#verificar si los numeros son pares o impares


def pares(a, b):
    return a + b

print(pares(8, 19))

def sumaArgs(*args):
    num = 0
    print(type(args))
    for arg in args:
        if str(arg).isdigit():
            num += arg
    return num


print(sumaArgs(6, 23, 65, 76, 87, 8,))

def ejemplo(*args):
    num = 0
    for arg in args:
        if type(arg) is int:
            if arg % 2 == 0:
                print ("tu número", arg, "es par")
            else:
                print("Tu numero", arg, "es impar")

