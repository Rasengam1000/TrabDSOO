import PySimpleGUI as sg

from Limite.TelaCarrinho import TelaCarrinho
from Entidade.Carrinho import Carrinho

class ControladorCarrinho:
    def __init__(self, controlador_sistema):
        self.__tela_carrinho = TelaCarrinho()
        self.__tela_produtos = controlador_sistema.controlador_produtos.tela_produtos
        self.__tela_clientes_cpf = controlador_sistema.controlador_clientes.telaclientes_cpf
        self.__controlador_sistema = controlador_sistema


    def incluir_compras(self):
        botao, cpf = self.__tela_clientes_cpf.open()
        self.__tela_clientes_cpf.close()
        if botao != "sair":
            try:
                cpf = int(cpf["cpf"])
                cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

                if cliente != None:
                    escolha = self.__controlador_sistema.controlador_produtos.produtos_disponiveis()
                    print(escolha)
                    cliente.carrinho.compras.append(escolha)
                    self.__controlador_sistema.DAOcliente.atualizar_carrinho()
                    self.__tela_carrinho.printar("Produto inserido com sucesso!")
                    self.__tela_produtos.close_selecionarwindow()
                else:
                    self.__tela_carrinho.printar("Cliente não existente!")
            except:
                self.__tela_carrinho.printar("O CPF deve ser numérico!")
        

    def excluir_compras(self):
        botao, cpf = self.__tela_clientes_cpf.open()
        self.__tela_clientes_cpf.close()
        if botao != "sair":
            try:
                cpf = int(cpf["cpf"])
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
                        try:
                            produto_selecionado = produto_selecionado[0][0].split()     #entrar no dicionario e entrar na lista e pegar a string
                        except:
                            self.__tela_carrinho.close_selecionarwindow()
                        else:
                            for produto in cliente.carrinho.compras:
                                if produto.codigo == int(produto_selecionado[0]):
                                    cliente.carrinho.compras.remove(produto)
                                    self.__controlador_sistema.DAOcliente.atualizar_carrinho()
                                    self.__tela_carrinho.printar(f"{produto.nome} excluído com sucesso")

                                    self.__tela_carrinho.close_selecionarwindow()
                                    return
            except:
                self.__tela_carrinho.printar("O CPF deve ser numérico!")

    def listar_compras(self):
        botao, cpf = self.__tela_clientes_cpf.open()
        self.__tela_clientes_cpf.close()
        if botao != "sair":
            try:
                cpf = int(cpf["cpf"])
                cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

                if cliente == None:
                    self.__tela_carrinho.printar("\nCPF informado não registrado!")

                else:
                    self.extrato(cliente)
            except:
                self.__tela_carrinho.printar("O CPF deve ser numérico!")
        

    def pagamento(self):
        botao, cpf = self.__tela_clientes_cpf.open()
        self.__tela_clientes_cpf.close()
        cpf = int(cpf["cpf"])
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

        while True:
            extrato, total = self.extrato(cliente)

            if cliente.tipo_cliente == "VIP":
                botao, valor = self.__tela_carrinho.pagar(cliente.carrinho.extrato, f"{0.75*total} (VIP - Desconto aplicado!)")
            else:
                botao, valor = self.__tela_carrinho.pagar()(cliente.carrinho.extrato, total)


            if botao == 1:
                cliente.carrinho.compras.clear()
                botao, excluir = self.__tela_carrinho.pegar_resposta("Deseja excluir a conta? (S/N): ")
                self.__tela_carrinho.close_getinfo()
                print(excluir)
                if excluir[0] == "S" or excluir[0] == "s":
                    self.__controlador_sistema.DAOcliente.remove(cliente)
                    self.__tela_carrinho.printar("Cliente excluído com sucesso")
                    break
            else:
                self.__tela_carrinho.close_getinfo()
            break

    def extrato(self,cliente):
        total = 0

        cliente.carrinho.extrato.clear()
        if cliente.carrinho.compras != [] and cliente.carrinho.compras != None:
            print(cliente.carrinho.compras)
            for produto in cliente.carrinho.compras:                                        #calculo extrato/preços
                cliente.carrinho.extrato.append(f"{produto.nome} R${produto.preco}")
                total += produto.preco
        return cliente.carrinho.extrato.append, total

    def voltar(self):
        self.__controlador_sistema.abre_tela()
    
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
