from abc import ABC, abstractmethod

class AbstractTela(ABC):

    @abstractmethod #sotestandoaa
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
                print('\nValor incorreto: Digite um número inteiro valido!')
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
                print('\nA opção só aceita números!')

    def verifica_letra(self, mensagem: str = ''):
        while True:
            valor_lido = input(mensagem)
            valor_lido_splitado = valor_lido.split()
            try:
                for item in valor_lido_splitado:
                    if not item.isalpha():
                        raise NameError
                return valor_lido
            except NameError:
                print('\nA opção só aceita letras!')

    def verifica_resposta(self, mensagem: str = '', respostas: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                if valor_lido not in respostas:
                    raise ValueError
                return valor_lido
            except ValueError:
                print('\nResposta incorreta: Digite uma resposta válida!')
                if respostas:
                    print('Respostas Válidas: ', respostas)