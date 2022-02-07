from limite.TelaCarrinho import TelaCarrinho
from entidade.Carrinho import Carrinho

class ControladorCarrinho:
    def __init__(self, controlador_sistema):
        self.__tela_carrinho = TelaCarrinho()
        self.__controlador_sistema = controlador_sistema


    def incluir_compras(self):
        cpf = self.__controlador_sistema.controlador_clientes.telaclientes.selecionar_cliente()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)
        
        escolha = self.__controlador_sistema.controlador_produtos.produtos_disponiveis()
        cliente.carrinho.compras.append(escolha)
        self.__tela_carrinho.printar("Produto inserido com sucesso!")
        

    def excluir_compras(self):
        cpf = self.__controlador_sistema.controlador_clientes.telaclientes.selecionar_cliente()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

        if cliente == None:
            self.__tela_carrinho.printar("\nCPF informado não registrado!")

        else:
            produto = self.__tela_carrinho.mostrar_info(cliente.carrinho.compras)
            cliente.carrinho.compras.remove(produto)
            self.__tela_carrinho.printar(f"{produto.nome} excluído com sucesso")


    def listar_compras(self):
        cpf = self.__controlador_sistema.controlador_clientes.telaclientes.selecionar_cliente()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

        if cliente == None:
            self.__tela_carrinho.printar("\nCPF informado não registrado!")

        else:
            self.extrato(cliente)
        

    def pagamento(self):
        cpf = self.__controlador_sistema.controlador_clientes.telaclientes.selecionar_cliente()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

        self.extrato(cliente)

        while True:
            pagou = self.__tela_carrinho.formas_pagamento()
            if pagou == "S":
                cliente.carrinho.compras.clear()
                excluir = self.__tela_carrinho.verifica_resposta("Deseja excluir a conta? (S/N): ", ["S", "N", "s", "n"]).upper()
                if excluir == "S":
                    self.__controlador_sistema.controlador_clientes.clientes.remove(cliente)
                    self.__tela_carrinho.printar("Cliente excluído com sucesso")
                    break
            else:
                continuar = self.__tela_carrinho.verifica_resposta("Deseja pagar mais tarde? (S/N): ", ["S", "N", "s", "n"]).upper()
                if continuar == "S":
                    break


    def voltar(self):
        self.__controlador_sistema.abre_tela()


    def extrato(self,cliente):
        total = 0
        cliente.carrinho.extrato.clear()
        if cliente.carrinho.compras != []:
            for produto in cliente.carrinho.compras:                                        #calculo extrato/preços
                cliente.carrinho.extrato.append(f"{produto.nome} - R$ {produto.preco}")
                total += produto.preco
        if cliente.tipo_cliente == "VIP":
            self.__tela_carrinho.mostrar_extrato(cliente.carrinho.extrato, f"{0.75*total} (VIP - Desconto aplicado!)")
        else:
            self.__tela_carrinho.mostrar_extrato(cliente.carrinho.extrato, total)


    def abre_tela(self):
        lista_opçoes = {0: self.voltar, 1: self.incluir_compras, 2: self.excluir_compras, 
                        3: self.listar_compras, 4: self.pagamento}

        while True:
            opçao = self.__tela_carrinho.opcoes()
            funçao = lista_opçoes[opçao]
            funçao()

    