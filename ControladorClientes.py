from ControladorPrincipal import ControladorPrinciapl
from TelaClientes import TelaClientes
from Cliente import Cliente

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
        self.listar_cliente()
        cpf_cliente = self.__telaclientes.selecionar_cliente()
        cliente = self.escolhe_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.__clientes.remove(cliente)
            self.listar_cliente()
        else:
            self.__telaclientes.mostra_mensagem('Cliente nao existente')

    def escolhe_cliente_por_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None              #pode ser util para outras coisas

    def alterar_cadastro(self):
        self.listar_cliente()
        cpf_cliente = self.__telaclientes.selecionar_cliente()
        cliente = self.escolhe_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            novo_cadastro = self.__telaclientes.pegar_info()
            cliente.nome = novo_cadastro['nome']
            cliente.sobrenome = novo_cadastro['sobrenome']
            cliente.cpf = novo_cadastro['cpf']
            cliente.idade = novo_cadastro['idade']
            self.listar_cliente()
        else:
            self.__telaclientes.mostra_mensagem('Cliente nao existente')

    def retornar(self):
        pass