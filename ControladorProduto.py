from TelaProduto import TelaProdutos
from Produto import Produto


class ControladorProdutos:
    def __init__(self, controlador_sistema):
        self.__tela_produtos = TelaProdutos()
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema

    def incluir_produto(self):
        codigo,nome,preco = self.__tela_produtos.pegar_info()#.split()
        if codigo == 0:
            self.__abre_tela
        else:
            self.__produtos.append(Produto(codigo,nome,preco))

    def excluir_produto(self):
        codigo = int(input("Qual o codigo do produto que deseja excluir?: "))
        for produto in self.__produtos:
            if produto.codigo == codigo:
                print(f"{produto.nome} excluído com sucesso")
                self.__produtos.remove(produto)
                break

    def listar_produtos(self):
        for produto in self.__produtos:
            self.__tela_produtos.mostrar_info(produto)

    def voltar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opçoes = {0: self.voltar, 1: self.incluir_produto, 2: self.excluir_produto, 
                        3: self.listar_produtos}

        while True:
            opçao = self.__tela_produtos.opçoes()
            funçao = lista_opçoes[opçao]
            funçao()
