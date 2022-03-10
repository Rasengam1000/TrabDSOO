from Limite.TelaClientes import TelaClientes
from Entidade.Cliente import Cliente
from Limite.TelaClientesAdc import TelaClientesAdc
from Limite.TelaClientesCpf import TelaClientesCpf
from Limite.TelaClientesAlt import TelaClientesAlt
from Limite.TelaClientesLista import TelaClientesLista


class ControladorClientes:

    def __init__(self, controladorprincipal):
        self.__controladorprincipal = controladorprincipal
        self.__telaclientes = TelaClientes()
        self.__telaclientes_adicionar = TelaClientesAdc()
        self.__telaclientes_cpf = TelaClientesCpf()
        self.__telaclientes_alt = TelaClientesAlt()
        self.__telaclientes_lista = TelaClientesLista()
        self.__clientes = self.__controladorprincipal.pCliente

    @property
    def telaclientes(self):
        return self.__telaclientes

    @property
    def clientes(self):
        return self.__clientes.cache
    def incluir_cliente(self):
        button, dados_cliente = self.__telaclientes_adicionar.open()
        self.__telaclientes_adicionar.close()
        self.checar_botao(button)
        if self.escolhe_cliente_por_cpf(dados_cliente['cpf']) is not None:
            self.__telaclientes.show_message('Erro', "CPF já cadastrado!")
        else:
            cliente = Cliente(dados_cliente['nome'], dados_cliente['sobrenome'], int(dados_cliente['cpf']),
                                  int(dados_cliente['idade']), dados_cliente['tipo_cliente'])
            self.__telaclientes.show_message('feito', 'Cliente Cadastrado')
            self.__controladorprincipal.pCliente.add(cliente)

    def listar_cliente(self):
        if self.__clientes.cache == []:
            self.__telaclientes.show_message('erro', 'Não existem clientes registrados')
        else:
            lista_pra_tela = []
            for teste in self.__clientes.cache:
                lista_pra_tela.append([teste.nome, teste.sobrenome, teste.cpf, teste.idade, teste.tipo_cliente])
            self.__telaclientes_lista.init_components(lista_pra_tela)
            self.__telaclientes_lista.open()

    def excluir_cliente(self):
        button, values = self.__telaclientes_cpf.open()
        self.__telaclientes_cpf.close()
        self.checar_botao(button)
        cpf_cliente = int(values['cpf'])
        cliente = self.escolhe_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            self.__controladorprincipal.pCliente.remove(cliente)
            self.__telaclientes.show_message('feito', 'Cliente excluído com sucesso')
        else:
            self.__telaclientes.show_message('erro', 'Cliente não existente')

    def escolhe_cliente_por_cpf(self, cpf: int):
        for cliente in self.__clientes.cache:
            if cliente.cpf == cpf:
                return cliente
        return None

    def alterar_cadastro(self):
        button, values = self.__telaclientes_cpf.open()
        self.__telaclientes_cpf.close()
        self.checar_botao(button)
        cpf_cliente = int(values['cpf'])
        cliente = self.escolhe_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            dados_cliente = {'nome': cliente.nome, 'sobrenome': cliente.sobrenome, 'idade':cliente.idade}
            self.__telaclientes_alt.init_components(dados_cliente)
            botao, novo_cadastro = self.__telaclientes_alt.open()
            self.__telaclientes_alt.close()
            self.checar_botao(botao)
            cliente.nome = novo_cadastro['nome']
            cliente.sobrenome = novo_cadastro['sobrenome']
            cliente.idade = novo_cadastro['idade']
            cliente.tipo_cliente = novo_cadastro['tipo_cliente']
            self.__telaclientes.show_message('feito', 'Cadastro alterado com sucesso')
        else:
            self.__telaclientes.show_message('erro', 'Cliente não existente')

    def info_cliente(self):
        button, values = self.__telaclientes_cpf.open()
        self.__telaclientes_cpf.close()
        self.checar_botao(button)
        cpf_cliente = int(values['cpf'])
        cliente = self.escolhe_cliente_por_cpf(cpf_cliente)
        if cliente is not None:
            lista_pra_tela = [[cliente.nome, cliente.sobrenome, cliente.cpf, cliente.idade, cliente.tipo_cliente]]
            self.__telaclientes_lista.init_components(lista_pra_tela)
            self.__telaclientes_lista.open()
        else:
            self.__telaclientes.show_message('erro', 'Cliente não existente')

    def retornar(self):
        self.__controladorprincipal.abre_tela()

    def abre_tela(self):

        lista_opcoes = {1: self.incluir_cliente, 2: self.excluir_cliente, 3: self.alterar_cadastro,
                        4: self.info_cliente, 5: self.listar_cliente, 0: self.retornar}

        while True:
            opcao_escolhida = self.__telaclientes.opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            self.__telaclientes.close()
            funcao_escolhida()

    def checar_botao(self, button):
        if button == 'sair' or button is None:
            self.abre_tela()

