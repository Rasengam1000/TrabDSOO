from limite.TelaPrincipal import TelaPrincipal

from controle.ControladorClientes import ControladorClientes
from controle.ControladorProduto import ControladorProdutos
from controle.ControladorCarrinho import ControladorCarrinho


class ControladorPrincipal:
    def __init__(self):
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__controlador_carrinho = ControladorCarrinho(self)

        self.__tela_sistema = TelaPrincipal()

    def iniciar_sistema(self):
        self.abre_tela()

    def encerrar_sistema():
        exit(0)

    def tela_cliente(self):
        self.__controlador_clientes.abre_tela()

    def tela_produtos(self):
        self.__controlador_produtos.abre_tela()

    def tela_carrinho(self):
        self.__controlador_carrinho.abre_tela()

    def abre_tela(self):
        lista_opçoes = {1: self.tela_cliente, 2: self.tela_produtos, 3: self.tela_carrinho,
                        0: self.encerrar_sistema}

        while True:
            opçao = self.__tela_sistema.opcoes()
            funçao = lista_opçoes[opçao]
            funçao()

    @property
    def controlador_clientes(self):
       return self.__controlador_clientes

    @property
    def controlador_produtos(self):
        return self.__controlador_produtos