import PySimpleGUI as sg

from Limite.TelaCarrinho import TelaCarrinho
from Entidade.Carrinho import Carrinho

class ControladorCarrinho:
    def __init__(self, controlador_sistema):
        self.__tela_carrinho = TelaCarrinho()
        self.__tela_produtos = controlador_sistema.controlador_produtos.tela_produtos
        self.__controlador_sistema = controlador_sistema


    def incluir_compras(self):
        cpf = self.__controlador_sistema.controlador_clientes.telaclientes.selecionar_cliente()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

        if cliente != None:
            escolha = self.__controlador_sistema.controlador_produtos.produtos_disponiveis()

            cliente.carrinho.compras.append(escolha)
            self.__controlador_sistema.DAOcliente.atualizar_carrinho()
            self.__tela_carrinho.printar("Produto inserido com sucesso!")
            self.__tela_produtos.close_selecionarwindow()
        else:
            self.__tela_carrinho.printar("Cliente não existente!")
        

    def excluir_compras(self):
        cpf = self.__controlador_sistema.controlador_clientes.telaclientes.selecionar_cliente()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

        if cliente == None:
            self.__tela_carrinho.printar("\nCPF informado não registrado!")

        else:
            if cliente.carrinho.compras != [] and cliente.carrinho.compras != None:
                carrinho_mostrar = []
                for produto in cliente.carrinho.compras:
                    produto_texto = f"{produto.codigo} - {produto.nome} - R$ {produto.preco}"
                    carrinho_mostrar.append(produto_texto)

                botao, produto_selecionado = self.__tela_carrinho.selecionar_produto(carrinho_mostrar)
                print(produto_selecionado)
                try:
                    print("trysplit")
                    produto_selecionado = produto_selecionado[0][0].split()     #entrar no dicionario e entrar na lista e pegar a string
                except:
                    print("except")
                    self.__tela_carrinho.close_selecionarwindow()
                else:
                    for produto in cliente.carrinho.compras:
                        print("forproduto")
                        if produto.codigo == int(produto_selecionado[0]):
                            print("produtoexiste")
                            cliente.carrinho.compras.remove(produto)
                            self.__controlador_sistema.DAOcliente.atualizar_carrinho()
                            self.__tela_carrinho.printar(f"{produto.nome} excluído com sucesso")

                            self.__tela_carrinho.close_selecionarwindow()
                            return
                


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
                    self.__controlador_sistema.DAOcliente.remove(cliente)
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
        if cliente.carrinho.compras != [] and cliente.carrinho.compras != None:
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

            if opçao[0] == None or opçao[0] == 0 or opçao[0] == sg.WIN_CLOSED:
                self.__tela_carrinho.close()
                break

            funçao = lista_opçoes[opçao[0]]
            funçao()

            self.__tela_carrinho.close()
