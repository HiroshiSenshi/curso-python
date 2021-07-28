*-*-*-*Listas y tuplas-*-*-*

Este artículo pretende una doble funcionalidad: introducir a aquellos nuevos en la programación o que estén migrando desde algún otro lenguaje al uso de Listas y Tuplas, como también a aquellos que lleven un tiempo con Python y quieran ampliar el tema y mejorar el código.

Para empezar, podría decirse que las Listas y Tuplas son lo que en otros lenguajes se llama vectores o arrays. Sin embargo, presentan varias diferencias.


*****Aplicación básica******
La diferencia
Una lista no es lo mismo que una tupla. Ambas son un conjunto ordenado de valores, en donde este último puede ser cualquier objeto: un número, una cadena, una función, una clase, una instancia, etc. La diferencia es que las listas presentan una serie de funciones adicionales que permiten un amplio manejo de los valores que contienen. Basándonos en esta definición, puede decirse que las listas son dinámicas, mientras que las tuplas son estáticas.

Crear una lista
Existen dos formas de hacerlo. La primera, es la convencional. La segunda, no recomiendo utilizarla, pero vale saber que existe.




---------Crear una lista--------
Existen dos formas de hacerlo. La primera, es la convencional. La segunda, no recomiendo utilizarla, pero vale saber que existe.

>>> a = []      # Sí.
>>> b = list()  # No.
>>> a == b      
True


Al utilizar los corchetes [] se crea una lista vacía, sin valores. Estos pueden especificarse durante la creación ingresándolos dentro de los corchetes y separados por comas.

a = [1, 2, 3, 4]
A cada uno de los valores, generalmente, se los llama elemento. Nótese que no es necesario indicar la cantidad de elementos que tiene o tendrá el objeto. En este caso, la lista cuenta con cuatro elementos numéricos. Sin embargo, tanto listas como tuplas pueden contener elementos de distintos tipos (incluso otras listas o tuplas), por ejemplo:

b = [5, "Hola mundo!", (1, 2), True, -1.5]


Crear una tupla
Al igual que en las listas hay dos formas de hacerlo:

>>> a = ()
>>> b = tuple()
>>> a == b
True

Como las tuplas son estáticas, debes especificar sus elementos durante la creación:

a = (5, "Hola mundo!", True, -1.5)
Si se quiere crear una tupla con un único elemento, debe añadirse una coma (,) antes de cerrar el paréntesis:

>>> b = (5,)  # Es una tupla
>>> type(b)
<type 'tuple'>
>>> c = (5)   # Es un número
>>> type(c)
<type 'int'>
Acceso a los elementos
Puedes acceder a los distintos elementos de una lista o tupla indicando el índice (comenzando desde el 0) entre corchetes.

>>> a = ["Hola", "mundo", "!"]
>>> a[0]
'Hola'
>>> a[1]
'mundo'
>>> a[2]
'!'
Si el índice está fuera del rango, obtendrás una excepción.

>>> a[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
Ya que a contiene tres elementos: el 0, el 1, y el 2.

Asignación de valores
Una vez creada una lista, puedes añadir cuantos valores desees.

>>> a = [1, 3, 5, 7]
>>> a.append(9)
>>> a
[1, 3, 5, 7, 9]
El método append agregará el elemento especificado al final de la lista.

Además, puedes modificar elementos existentes, combinando el método de acceso con el de asignación:




Sacado de :


 https://recursospython.com/guias-y-manuales/listas-y-tuplas/

 https://www.analyticslane.com/2019/09/27/diferencia-entre-listas-y-tuplas-en-python/

https://uniwebsidad.com/libros/python/capitulo-7/anexo-sobre-listas-y-tuplas









