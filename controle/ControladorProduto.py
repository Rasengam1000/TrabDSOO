from limite.TelaProduto import TelaProdutos
from entidade.Produto import Produto


class ControladorProdutos:
    def __init__(self, controlador_sistema):
        self.__tela_produtos = TelaProdutos()
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema

    @property
    def produtos(self):
        return self.__produtos

    def produtos_disponiveis(self):
        produto = self.__tela_produtos.mostrar_produtos(self.__produtos)
        return produto

    def incluir_produto(self):
        codigo,nome,preco = self.__tela_produtos.pegar_info()
        tem = 0
        for produto in self.__produtos:
            if produto.codigo == int(codigo):
                print("Um produto já foi registrado com esse código!")
                tem = 1
        if tem == 1:
            self.abre_tela()
        else:
            self.__produtos.append(Produto(codigo,nome,preco))
            print("Produto inserido com sucesso!")

    def excluir_produto(self):
        codigo = self.__tela_produtos.selecionar_produto(self.__produtos)
        for produto in self.__produtos:
            if produto.codigo == codigo:
                self.__produtos.remove(produto)
                self.__tela_produtos.printar(f"\n{produto.nome} excluído com sucesso")
                return

        self.__tela_produtos.printar("\nCodigo informado não encontrado!")

    def listar_produtos(self):
        self.__tela_produtos.printar("")
        for produto in self.__produtos:
            self.__tela_produtos.mostrar_info(produto)

    def voltar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opçoes = {0: self.voltar, 1: self.incluir_produto, 2: self.excluir_produto, 
                        3: self.listar_produtos}

        while True:
            opçao = self.__tela_produtos.opcoes()
            funçao = lista_opçoes[opçao]
            funçao()
