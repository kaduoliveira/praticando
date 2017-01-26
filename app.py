# -*- coding: UTF-8 -*-

def listar(nomes):
    print('Listando os nomes da lista:')
    for nome in nomes:
        print(nome)
    print('\n')

def cadastrar(nomes):
    print('Digite o nome:')
    nome = input()
    nomes.append(nome)

def remover(nomes):
    print('Qual nome vocÊ gostaria de remover?')
    nome = input()
    nome_string = str(nome)
    nomes.remove(nome_string)
    print('Lista atualizada')
    print(nomes)

def alterar(nomes):
    print('Qual o nome você gostária de editar:')
    nome = input()
    teste = nome in nomes #verificando a existemcia do nome pesquisado na lista
    if(teste == True):  
        #posicao = nomes.index(nome)
        print(posicao)  #detecting the position on the list
        novo_nome = input('Digite o novo nome: ')
        nomes[posicao] = novo_nome  #using the position as a reference to change the right iten on the list
        print('Lista atualizada:')
        print(nomes)
    else:
        print('Este nome não existe na lista')

def buscar(nomes):
    import re
    print('Digite o texto da busca:')
    busca = input()
    resultado = re.findall('(\w' + busca + '\w+)', nomes)
    if(resultados != None):
        print('Apesquisa pertence a lista.')
    
    

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print('Digite 1 para CADASTRAR, 2 para LISTAR, 3 para REMOVER, 4 para EDITAR, 5 para BUSCAR e 0 para ENCERRAR: ')
        escolha = input()
        
        if(escolha == '1'):
            cadastrar(nomes)
        
        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            remover(nomes)

        if(escolha == '4'):
            alterar(nomes)
        
        if(escolha == '5'):
            buscar(nomes)
menu()            