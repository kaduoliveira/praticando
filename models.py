# -*- codiing: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, tel, empresa):
        self.nome = nome
        self.tel = tel
        self.empresa = empresa
    
    def imprimir(self):
        print('Nome:' + self.nome + ' Tel:' + self.tel + ' Empresa:' + self.empresa)

class Data(object):
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
        print(self.dia + '/' + self.mes + '/' + self.ano)
