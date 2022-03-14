from Limite.TelaPrincipal import TelaPrincipal

from Controle.ControladorClientes import ControladorClientes
from Controle.ControladorProduto import ControladorProdutos
from Controle.ControladorCarrinho import ControladorCarrinho

from Persistencia.DataSource import DataSource
from Persistencia.DAOcliente import DAOcliente
from Persistencia.DAOproduto import DAOproduto


class ControladorPrincipal:
    def __init__(self):   
        self.__DAOcliente = DAOcliente()
        self.__DAOproduto = DAOproduto()

        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__controlador_carrinho = ControladorCarrinho(self)
        
        self.__tela_sistema = TelaPrincipal()

    def iniciar_sistema(self):
        self.abre_tela()

    def encerrar_sistema(self):
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
            self.__tela_sistema.close()
            funçao()

    @property
    def controlador_clientes(self):
       return self.__controlador_clientes

    @property
    def controlador_produtos(self):
        return self.__controlador_produtos

    @property
    def DAOproduto(self):
        return self.__DAOproduto

    @property
    def DAOcliente(self):
        return self.__DAOcliente