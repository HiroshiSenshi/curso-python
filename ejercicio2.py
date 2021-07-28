# python code to demonstrate working of reduce()
# using operator functions
 
# importing functools for reduce()
import functools
 
# importing operator for operator functions
import operator
 
# initializing list
lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute sum of list
# using operator functions
print("La suma de los elementos es : ", end="")
print(functools.reduce(operator.add, lis))
 
# using reduce to compute product
# using operator functions
print("El producto de los elementos de la lista es:: ", end="")
print(functools.reduce(operator.mul, lis))
 
# using reduce to concatenate string
print("El producto concatenado es: ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

