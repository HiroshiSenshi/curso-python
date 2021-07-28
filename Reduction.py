# python code to demonstrate working of reduce()
 
# importing functools for reduce()
#import functools
from functools import reduce
# initializing list
lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute sum of list
print("La suma de los elementos de la lista es : ", end="")
print(reduce(lambda a, b: a+b, lis))
 
# using reduce to compute maximum element from list
print("El maximo elemento de la lista es  : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))

