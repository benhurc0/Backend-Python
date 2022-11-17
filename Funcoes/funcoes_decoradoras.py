## decoradoras servem para potencializar (dar mais recursos) para outras funções
# para utilizar uma função decoradora utilizar o @ antes do nome da função
# e em cima da função que sera decorada (receberá os poderes da outra função)

## criar a função decoradora

def master(msg):
    def imprime():
        print('Essa é a função Decoradora')
        msg()
    return imprime

## segunda função que vai ser utilizada junto com a decoradora
@master
def funcao_simples():
    print('Estou chamando a função simples')
funcao_simples()            