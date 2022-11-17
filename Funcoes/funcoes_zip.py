## zip manipula e mescla estruturas de dados
# e seus valores. Poderem o resultado sempre será da 
# o valor da menor estrutura de dados.

dicverduras = {1:'Cebola',2:'alface',3:'Repolho',4:'Beterraba'}
dicfrutas = {1:'Maça',2:'Laranja',3:'Pera'}

mescla = list(zip(dicverduras,dicfrutas))

print(mescla)

mesclavalores = list(zip(dicverduras.values(),dicfrutas.values()))

print(mesclavalores)

## Iterar valores

for p in mesclavalores:
    print(p)