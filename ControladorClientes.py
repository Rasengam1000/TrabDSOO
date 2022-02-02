from ControladorPrincipal import ControladorPrinciapl
from TelaClientes import TelaClientes

class ControladorClientes:

    def __init__(self, controladorprincipal: ControladorPrincipal):
        self.__controladorprincipal = controladorprincipal
        self.__telaclientes = TelaClientes(self)
        self.__clientes = []

    def incluir_cliente(self):
        dados_cliente = self.__telaclientes.pegar_info()
        cliente = Cliente(dados_cliente['nome'], dados_cliente['sobrenome'], dados_cliente['cpf'],
                          dados_cliente['idade'])
        self.__clientes.append(cliente)

    def listar_cliente(self):
        if self.__clientes == []:
            self.__telaclientes.mostra_mensagem('Nao existem clientes registrados')
        else:
            for cliente in self.__clientes:
                self.__telaclientes.mostrar_info({'nome': cliente.nome, 'sobrenome': cliente.sobrenome,
                                                  'cpf': cliente.cpf, 'idade': cliente.idade})

    def excluir_cliente(self):
        pass



