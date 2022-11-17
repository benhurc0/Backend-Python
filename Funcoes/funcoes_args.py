## *args saõ utilizadas quando não sabemos o números 
# de argumentos necessários em uma função e retorna tupla

def soma(*args):
    print(args)


soma(1,3,2,42,1,2,53,12,2)

def soma_total(*args):
    total = 0
    for n in args:
        total += n
    return total

print(soma_total(1,3,7,5,10))        