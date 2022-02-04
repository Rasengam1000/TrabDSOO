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

    def pegar_info(self):
        print('Dados Cliente')
        nome = self.verifica_letra('Nome: ')
        sobrenome = self.verifica_letra('Sobrenome: ')
        cpf = self.verifica_algarismo('CPF: ')
        idade = self.verifica_algarismo('Idade: ')
        tipo_cliente = self.verifica_resposta('Deseja comprar VIP?: ', ['sim', 'nao'])
        if tipo_cliente == 'sim':
            tipo_cliente = 'vip'
        else:
            tipo_cliente = 'comum'
        return{'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'idade': idade, 'tipo_cliente': tipo_cliente}

    def mostrar_info(self, dados_cliente):
        print('Nome do Cliente: ', dados_cliente['nome'])
        print('Sobrenome do Cliente: ', dados_cliente['sobrenome'])
        print('CPF do Cliente: ', dados_cliente['cpf'])
        print('Idade do Cliente: ', dados_cliente['idade'])
        print('Tipo do CLiente: ', dados_cliente['tipo_cliente'])
        print()

    def selecionar_cliente(self):
        cpf = self.verifica_algarismo('CPF do cliente desejado: ')
        return cpf