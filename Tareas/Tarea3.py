Los diccionarios y conjuntos son ambos tipos de datos en Python. Pueden usar comprensión como lista por comprensión. Echa un vistazo a esta entrada para obtener más información sobre lista por comprensión.

Conjuntos
Un conjunto es una lista de elementos únicos que no están ordenados. Conjuntos aceptan operaciones matemáticas como unión, diferencia, intersección y diferencia simétrica. También, puede hacer pruebas de membresía con conjuntos. Es importante observar que un conjunto vacío es set(). De otra manera, puede usar llaves para rodear elementos para crear un conjunto.

Ejemplos:

terminos = set() # un conjunto vacío
terminos = {'hane', 'gote', 'joseki', 'hane'}
terminos #duplicados son eliminados
{'hane', 'gote', 'joseki'}
'hane' in terminos #pruebas de membresía
True
moviementos = {'gote', 'sente', 'hane'}
moviementos|terminos #unión
{'hane', 'sente', 'gote', 'joseki'}
moviementos&terminos #intersección
{'hane', 'gote'}
moviementos-terminos #diferencia
{'sente'}
moviementos^terminos #diferencia simétrica
{'joseki', 'sente'}
 

Diccionarios
Un diccionario es una colección desordenada de parejas (clave:valor). En otros lenguajes de programaciones, un diccionario puede ser llamado una matriz asociativa. La clave tiene que ser un objeto inmutable mientras que el valor puede ser mutable. Un diccionario vacío se muestra por {}. Hay tres formas diferentes de escribir un diccionario en Python. Ellos son:

diccionario1 = {'a':'b', 'c':'d', 'e':'f'}
diccionario2 = dict([('a','b'), ('c','d'), ('e','f')])
diccionario3 = dict (a='b', c='d', e='f')
Puedes sobreescribir un par clave-valor y eliminar un par clave-valor, también.

diccionario1['a'] = 'nuevo' #sobreescribir
del(diccionario1['c']) #elimina el par c-d
Diccionarios tienen un complejidad O(1), y están optimizados para la sobrecarga de memoria. Hay una tabla de funciones y metodos internos, abajo.


Sacado de :

http://www.pybasico.com/python/python-conjuntos-diccionarios/

https://recursospython.com/guias-y-manuales/conjuntos-sets/

https://nicolas2324.wordpress.com/2012/09/30/python-conjuntos-y-diccionarios/

https://devcode.la/tutoriales/diccionarios-en-python/

http://docs.python.org.ar/tutorial/3/datastructures.html