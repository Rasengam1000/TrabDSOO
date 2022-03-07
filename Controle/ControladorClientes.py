from Limite.TelaClientes import TelaClientes
from Entidade.Cliente import Cliente

class ControladorClientes:

    def __init__(self, controladorprincipal):
        self.__controladorprincipal = controladorprincipal
        self.__telaclientes = TelaClientes()
        self.__clientes = []

    @property
    def telaclientes(self):
        return self.__telaclientes

    @property
    def clientes(self):
        return self.__clientes

    def incluir_cliente(self):
        dados_cliente = self.__telaclientes.pegar_info()
        if self.escolhe_cliente_por_cpf(dados_cliente['cpf']) != None:
            print("\nCPF já cadastrado!\n")
        else:
            cliente = Cliente(dados_cliente['nome'], dados_cliente['sobrenome'], dados_cliente['cpf'],
                              dados_cliente['idade'], dados_cliente['tipo_cliente'])
            self.__clientes.append(cliente)

    def listar_cliente(self):
        if self.__clientes == []:
            self.__telaclientes.mostra_mensagem('\nNão existem clientes registrados')
        else:
            for cliente in self.__clientes:
                self.__telaclientes.mostrar_info({'nome': cliente.nome, 'sobrenome': cliente.sobrenome,
                                                  'cpf': cliente.cpf, 'idade': cliente.idade,
                                                  'tipo_cliente': cliente.tipo_cliente})

    def excluir_cliente(self):
        cpf_cliente = self.__telaclientes.selecionar_cliente()
        cliente = self.escolhe_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.__clientes.remove(cliente)
            self.__telaclientes.mostra_mensagem('\nCliente excluído com sucesso')
        else:
            self.__telaclientes.mostra_mensagem('\nCliente não existente')

    def escolhe_cliente_por_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def alterar_cadastro(self):
        cpf_cliente = self.__telaclientes.selecionar_cliente()
        cliente = self.escolhe_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            novo_cadastro = self.__telaclientes.pegar_info()
            cliente.nome = novo_cadastro['nome']
            cliente.sobrenome = novo_cadastro['sobrenome']
            cliente.cpf = novo_cadastro['cpf']
            cliente.idade = novo_cadastro['idade']
            cliente.tipo_cliente = novo_cadastro['tipo_cliente']
            self.__telaclientes.mostra_mensagem('\nCadastro alterado com sucesso')
        else:
            self.__telaclientes.mostra_mensagem('\nCliente não existente')

    def info_cliente(self):
        cpf_cliente = self.__telaclientes.selecionar_cliente()
        cliente = self.escolhe_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.__telaclientes.mostrar_info({'nome': cliente.nome, 'sobrenome': cliente.sobrenome,
                                              'cpf': cliente.cpf, 'idade': cliente.idade,
                                              'tipo_cliente': cliente.tipo_cliente})
        else:
            self.__telaclientes.mostra_mensagem('\nCliente não existente')

    def retornar(self):
        self.__controladorprincipal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.excluir_cliente, 3: self.alterar_cadastro,
                        4: self.info_cliente, 5: self.listar_cliente, 0: self.retornar}

        while True:
            lista_opcoes[self.__telaclientes.opcoes()]()