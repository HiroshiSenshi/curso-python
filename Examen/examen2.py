#1. 

def frase (string):
    my_set = set(())
    for i in string:
        if (set(i).issubset(my_set)) == False:
            my_set.add(i)
        else:
            print("Tu string: '" + string + "', no son caractes unicos.\n")
            return

    print("Tu string: '" + string + "', si tiene caracteres únicos!\n")

frase("Hiro Se la pasa durmiendo")
frase("Pulsar")

#2. 

def precioalto (dicconario):
    value = 0
    for i in dicconario: 
        aux = dicconario.get(i)
        if value <= aux:
            value = aux 
        else:
            pass
    my_keys = list(dicconario.keys())
    my_values = list(dicconario.values())
    objeto = my_values.index(value)
    print("el producto que cuesta mas  es:", my_keys[objeto],"este articulo tiene un valor de: $", my_values[objeto],)

precioalto({'iphone 11' : 115000, 'xiomi redmi 6' : 67000, 'motorola one plus' : 4300, 'ipad pro' : 10000, 'laptop gaming' : 10000})


#3. 

def verificador(cadena):
    ahs_true = "ahs"
    ahs_false = ".ahs"
    if ahs_false in cadena:
        return False
    elif ahs_true in cadena:
        return True

prueba = "esdfahs"
print(verificador(prueba))

#4. 


def nombre(str1, str2):
    str1 = str1.replace('*','').replace('?','').replace('!','').replace('-','').replace(' ','').capitalize()
    str2 = str2.replace('*','').replace('?','').replace('!','').replace('-','').replace(' ','').capitalize()
    
    if len(str1) == len(str2):
        print(str1 + ", " + str2 + "\n")

    elif len(str1) < len(str2):
        print(str1 + str2 + str1 + "\n")
    else: 
        print(str2 + str1 + str2 + "\n")
        

nombre("-pancho***","?Pis!tolas")


#5. 

def quitarele(string, int): 
    my_list = list(string) 
    for i in range(int):
        my_list.pop()
    my_list = "".join(my_list)
    print(my_list)

quitarele("El arbol saca manzanas",10)
quitarele("El arbol saca manzanas",7)
quitarele("El arbol saca manzanas",0)