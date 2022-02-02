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

    def pegar_info(self): #ver se precisa verificar
        print('Dados Cliente')
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        cpf = input('CPF: ')
        idade = input('Idade: ')

        return{'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'idade': idade}

    def mostra_mensagem(self, msg):  #pode ser util colocar na abstract
        print(msg)

    def mostrar_info(self, dados_cliente):
        print('Nome do Cliente: ', dados_cliente['nome'])
        print('Sobrenome do Cliente ', dados_cliente['sobrenome'])
        print('CPF do Cliente ', dados_cliente['cpf'])
        print('Idade do Cliente ', dados_cliente['idade'])
        print()   #espaco em branco

    def selecionar_cliente(self): #continuar daqui
        pass