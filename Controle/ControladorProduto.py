import PySimpleGUI as sg

from Limite.TelaProduto import TelaProdutos
from Entidade.Produto import Produto


class ControladorProdutos:
    def __init__(self, controlador_sistema):
        self.__tela_produtos = TelaProdutos()
        self.__controlador_sistema = controlador_sistema
        self.__produtos = controlador_sistema.DAOproduto

    @property
    def produtos(self):
        return self.__produtos.cache

    @property
    def tela_produtos(self):
        return self.__tela_produtos

    def produtos_disponiveis(self):
        produtos_mostrar = []
        for produto in self.__produtos.cache:
            produto_texto = produto.codigo, produto.nome, f"R${produto.preco}"
            produtos_mostrar.append(produto_texto)
        botao, produto_selecionado = self.__tela_produtos.selecionar_produto(produtos_mostrar)
        
        try:
            print(produto_selecionado)
            produto_selecionado = produto_selecionado[0][0][0]     #entrar no dicionario e entrar na lista e pegar a string
        except:
            self.__tela_produtos.close_selecionarwindow()
        else:
            if botao == 1:
                print("botao1")
                for produto in self.__produtos.cache:
                    if produto.codigo == int(produto_selecionado):
                        print("produto sendo inserido")
                        return produto

                self.__tela_produtos.printar("\nCódigo informado não encontrado!")

            elif botao == "00":
                self.__tela_produtos.close_selecionarwindow()

    def incluir_produto(self):
        try:
            self.__tela_produtos.close()
            codigo,nome,preco = self.__tela_produtos.pegar_info()[1].values()
            tem = 0

            for produto in self.__produtos.cache:
                if produto.codigo == int(codigo):
                    self.__tela_produtos.printar("Um produto já foi registrado com esse código!")
                    tem = 1
            if tem == 1:
                self.abre_tela()
            else:
                print("hora de inserir")
                self.__produtos.add(Produto(codigo,nome,preco))
                self.__tela_produtos.printar("Produto inserido com sucesso!")

            self.__tela_produtos.close_getinfo()
        except:
            self.__tela_produtos.close_getinfo()

    def excluir_produto(self):
        produtos_mostrar = []
        for produto in self.__produtos.cache:
            produto_texto = f"{produto.codigo} | {produto.nome} | R${produto.preco}"
            produtos_mostrar.append(produto_texto)

        self.__tela_produtos.close()
        botao, produto_selecionado = self.__tela_produtos.selecionar_produto(produtos_mostrar)

        try:
            produto_selecionado = produto_selecionado[0][0].split()     #entrar no dicionario e entrar na lista e pegar a string
        except:
            self.__tela_produtos.close_selecionarwindow()
        else:
            if botao == 1:
                for produto in self.__produtos.cache:
                    if produto.codigo == int(produto_selecionado[0]):
                        self.__produtos.remove(produto)
                        self.__tela_produtos.printar(f"\n{produto.nome} excluído com sucesso")
                        self.__tela_produtos.close_selecionarwindow()
                        return
                self.__tela_produtos.printar("\nCódigo informado não encontrado!")

            elif botao == "00":
                self.__tela_produtos.close_selecionarwindow()

    def listar_produtos(self):
        produtos_mostrar = []
        for produto in self.__produtos.cache:
            produto_texto = produto.codigo, produto.nome, f"R${produto.preco}"
            produtos_mostrar.append(produto_texto)

        self.__tela_produtos.close()
        botao = self.__tela_produtos.mostrar_info(produtos_mostrar)

        if botao[0] == "00":
            self.__tela_produtos.close_info()

    def voltar(self):
        self.__tela_produtos.close()

    def abre_tela(self):
        lista_opçoes = {0: self.voltar, 1: self.incluir_produto, 2: self.excluir_produto, 
                        3: self.listar_produtos}

        while True:
            opçao = self.__tela_produtos.opcoes()

            if opçao[0] == None or opçao[0] == 0 or opçao[0] == sg.WIN_CLOSED:
                self.__tela_produtos.close()
                break

            funçao = lista_opçoes[opçao[0]]
            funçao()
                
            self.__tela_produtos.close()
