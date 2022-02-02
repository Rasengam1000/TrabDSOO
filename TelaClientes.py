from AbstractTela import AbstractTela
from ControladorClientes import ControladorClientes

class TelaClientes(AbstractTela):

    def __init__(self, controlador: ControladorClientes):
        self.__controlador = controlador

    def opcoes(self):
        print('----------- Clientes -----------')
        print('1 - Incluir Cliente')
        print('2 - Excluir Cliente')
        print('3 - Alterar Cadastro')
        print('4 - Informacao Cliente')
        print('5 - Listar Clientes')
        print('0 - Retornar')
        opcao = self.verifica_num_int('Escolha a opcao: ', [1, 2, 3, 4, 5, 0])
        return opcao