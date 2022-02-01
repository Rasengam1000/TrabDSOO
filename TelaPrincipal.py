from AbstractTela import AbstractTela
from ControladorPrincipal import ControladorPrincipal

class TelaPrincipal(AbstractTela):

    def __init__(self, controlador: ControladorPrincipal): #cuidar para o controlador se enviar para criacao da classe
        self.__controlador = controlador

    def opcoes(self):
        print('----------- Balada mamacos ----------') # mudar o nome kkkkk
        print('Escolha sua opcao')
        print('1 - Clientes')
        print('2 - Produtos')
        print('3 - Carrinho')
        print('0 - Encerrar Sistema')
        opcao = self.verifica_num_int('Escolha a opcao: ', [1, 2, 3, 0]) #olhar o controlador nisso tbm
        return opcao