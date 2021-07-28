Entendiendo **kwargs
Veamos ahora el uso de **kwargs como parámetro.

En Python, el parámetro especial **kwargs en una función se usa para pasar, de forma opcional, un número variable de argumentos con nombre.

Las principales diferencias con respecto *args son:

Lo que realmente indica que el parámetro es de este tipo es el símbolo ‘**’, el nombre kwargs se usa por convención.
El parámetro recibe los argumentos como un diccionario.
Al tratarse de un diccionario, el orden de los parámetros no importa. Los parámetros se asocian en función de las claves del diccionario.
¿Cuándo es útil su uso?

Imaginemos que queremos implementar una función filter que nos devuelva una consulta SQL de una tabla clientes que tiene los siguientes campos: nombre, apellidos, fecha_alta, ciudad, provincia, tipo y fecha_nacimiento.

Una primera aproximación podría ser la siguiente:

def filter(ciudad, provincia, fecha_alta):
    return "SELECT * FROM clientes WHERE ciudad='{}' AND provincia='{}' AND fecha_alta={};".format(ciudad, provincia, fecha_alta)
No es una función para sentirse muy contento 😖 Entre los diferentes problemas que pueden surgir tenemos:

Si queremos filtrar por un nuevo parámetro, hay que cambiar la definición de la función así como la implementación.
Los parámetros son todos obligatorios.
Si queremos consultar otro tipo de clientes manteniendo esta consulta, debemos crear una nueva función.
La solución a todos estos problemas está en hacer uso del parámetro **kwargs. Veamos cómo sería la nueva función filter usando **kwargs:

def filter(**kwargs):
    query = "SELECT * FROM clientes"
    i = 0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE "
        else:
            query += " AND "
        query += "{}='{}'".format(key, value)
        i += 1
    query += ";"
    return query
Con esta nueva implementación hemos resuelto todos nuestros problemas como auténticos pythonistas 😄🐍

A continuación podemos ver cómo se comporta la nueva función filter:

>>>filter()
SELECT * FROM clientes;
>>>filter(ciudad="Madrid")
SELECT * FROM clientes WHERE ciudad='Madrid';
>>>filter(ciudad="Madrid", fecha_alta="25-10-2018")
SELECT * FROM clientes WHERE ciudad='Madrid' AND fecha_alta='25-10-2018';
Hasta aquí hemos visto qué significan los parámetros *args y **kwargs en una función en Python y dos ejemplos de cuándo y cómo usarlos. Otros ejemplos de uso comunes son los decoradores (de los cuáles te hablaré en otro post) y el método __init__ en la herencia. Te mostraré este último ya que hace un uso combinado de ambos.

Supongamos que tenemos la siguiente clase Punto:

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return "x: {}, y: {}".format(self.x, self.y)
Y ahora queremos añadir una clase Circulo que herede de Punto. Para conocer todos los detalles del círculo, nos hace falta conocer su radio, por lo que debe ser incluido en el método __init__. Sin embargo, la definición será un poco diferente a la de la clase Punto:

class Circulo(Punto):
    def __init__(self, radio, *args, **kwargs):
        self.radio = radio
        super().__init__(*args, **kwargs)
    def __repr__(self):
        return "x: {}, y: {}, radio: {}".format(self.x, self.y, self.radio)
Con esta implementación, si la definición del método __init__ en la clase Punto cambia, no tendremos que modificar la implementación de la clase Circulo.

Para crear un objeto de la clase Circulo basta con escribir:

>>>Circulo(10, 1, 1)
x: 1, y: 1, radio: 10
En otros post veremos más sobre herencia y orientación a objetos en el lenguaje Python. Con este ejemplo simplemente quería mostrar otro uso de los parámetros *args y **kwargs.

El orden importa
Quiero mencionar que el orden de los parámetros *args y **kwargs en la definición de una función importa, y mucho. Ambos pueden aparecer de forma conjunta o individual, pero siempre al final y de la siguiente manera:

def ejemplo(arg1, arg2, *args, **kwargs)
*args y **kwargs como argumentos en la llamada a una función
*args y **kwargs también pueden usarse como argumentos al invocar a una función y su comportamiento es distinto al que te he enseñado anteriormente.

Imaginemos la siguiente función resultado:

def resultado(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
Esta función recibe tres parámetros: x, y y op y puede ser invocada de distintas formas. La primera de ellas es la que ya supones:

>>>resultado(1, 2, '+')
3
Pero también podemos invocar a la función resultado con un único parámetro de tipo iterable, como una tupla o una lista, del siguiente modo (*args):

>>>a = (1, 2, '+')
>>>resultado(*a)
3
O incluso así:

>>>a = (2, '-')
>>>resultado(3, *a)
1
También podemos pasar como argumento un diccionario usando como claves los nombres de los parámetros (**kwargs):

>>>a = {"op": "+", "x": 2, "y": 5}
>>>resultado(**a)
7
Conclusión
Bueno, con esto llega a su fin el tutorial sobre qué significan y cómo y cuándo usar los parámetros *args y **kwargs en Python. Repasemos las cuestiones clave:

Utiliza *args para pasar de forma opcional a una función un número variable de argumentos posicionales.
El parámetro *args recibe los argumentos como una tupla.
Emplea **kwargs para pasar de forma opcional a una función un número variable de argumentos con nombre.
El parámetro **kwargs recibe los argumentos como un diccionario.
Por último, quiero comentarte que un gran poder conlleva una gran responsabilidad. Utilizar *args y **kwargs puede ahorrarte muchos mareos de cabeza y convertirte en un programador top pero también puede llevarte a resultados inesperados si no llevas cuidado con su uso.


Sacado de :
https://j2logo.com/args-y-kwargs-en-python/