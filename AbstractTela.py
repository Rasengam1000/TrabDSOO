from abc import ABC, abstractmethod

class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def opcoes(self):
        pass

    def verifica_num_int(self, mensagem: str = '', inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print('Valor incorreto: Digite um numero inteiro valido')
                if inteiros_validos:
                    print('Valores Validos: ', inteiros_validos)

    def mostra_mensagem(self, msg):
        print(msg)

    def verifica_algarismo(self, mensagem: str = ''):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                return inteiro
            except ValueError:
                print('A opcao so aceita numeros')

    def verifica_letra(self, mensagem: str = ''):
        while True:
            valor_lido = input(mensagem)
            try:
                if not valor_lido.isalpha():
                    raise NameError
                return valor_lido
            except NameError:
                print('A opcao so aceita letras')