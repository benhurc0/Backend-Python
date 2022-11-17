## Funções Kwargs  
# passar um número inderteminado de parametros
# para uma função. diferente de arg precisa passar nos argumentos identificador de chaves e valores

def saudacoes(**Kwargs):
    print(Kwargs)

saudacoes(manha='bom dia', tarde='boa tarde')

def saudacao_dia(**kwargs):
    for periodo_dia,saudacao in kwargs.items():
        print(f'Durante a {periodo_dia} dizemos {saudacao}')

saudacao_dia(manha='bom dia', tarde='boa tarde', noite='boa noite', madrugada='vai dormir')