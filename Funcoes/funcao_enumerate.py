# enumerate enumera indice de estruturas de dados
# retornae o indice de uma lista

animais = ['Cachorro', 'Gato', 'Periquito', 'Elefante']

print(list(enumerate(animais)))

## Iterar com o enumerate

for i, valor in enumerate(animais):
    print(i,valor)

 ## Iterador e enumerate com condicionais

for i, valor in enumerate(animais):
    if i >2:
        break
    else:
        print(valor)   