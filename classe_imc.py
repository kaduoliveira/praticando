class Pessoa(object):
    'Classe padrão para cálculos basais'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimi_imc(self):
        calculo_imc = self.peso / (self.altura * self.altura)
        print('Olá, ', self.nome, '. Você, pesando ', self.peso, 'kg e medindo ', self.altura, 'mt, tem um imc de ', calculo_imc, '.')