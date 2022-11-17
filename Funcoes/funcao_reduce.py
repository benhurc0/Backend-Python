# reduce serve para reduzir os valores de uma estruturas de dados a um unico valor
# precisamos importar um modulo builtin chamado functools

from functools import reduce

lista = [2,7,10,6,78]

def mult(x,y):
    return x*y

print(reduce(mult,lista))

list2 = [30,67,1000,61,98]

testmaior = lambda x,y: x if (x>y) else y

print(reduce(testmaior,list2))