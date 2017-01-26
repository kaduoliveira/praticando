
'''
versao 1
def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    print(parte1, parte2)
'''

def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(convite):
    nome_convite = gera_nome_convite()
    print(convite)

def cadastrar(nomes):
    print('Digite o nome:')
    nome = input()
    nomes.append(nome)

