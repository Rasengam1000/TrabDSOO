from Limite.TelaPrincipal import TelaPrincipal

from Controle.ControladorClientes import ControladorClientes
from Controle.ControladorProduto import ControladorProdutos
from Controle.ControladorCarrinho import ControladorCarrinho

from Persistencia.pMain import Pmain
from Persistencia.pCliente import Pcliente
from Persistencia.pProduto import Pproduto


class ControladorPrincipal:
    def __init__(self):
        self.__pMain = Pmain()
        self.__pCliente = Pcliente(self.__pMain)
        self.__pProduto = Pproduto(self.__pMain)
        self.abrir_persistencia()

        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__controlador_carrinho = ControladorCarrinho(self)
        
        self.__tela_sistema = TelaPrincipal()

    def iniciar_sistema(self):
        self.abre_tela()

    def encerrar_sistema(self):
        self.__pMain.guardar()
        exit(0)

    def abrir_persistencia(self):
        self.__pMain.abrir()
        self.__pCliente.abrir()
        self.__pProduto.abrir()

    def tela_cliente(self):
        self.__controlador_clientes.abre_tela()

    def tela_produtos(self):
        self.__controlador_produtos.abre_tela()

    def tela_carrinho(self):
        self.__controlador_carrinho.abre_tela()
    
    def dev(self):
        opçao = int(input("1- apagar persist\n2- print cache main e locais"))
        if opçao == 1:
            opçao = int(input("\n1- cliente\n2- produto\n3- tudo\n"))
            if opçao == 1:
                self.__pCliente.apagar()
            elif opçao == 2:
                self.__pProduto.apagar()
            elif opçao == 3:
                self.__pCliente.apagar()
                self.__pProduto.apagar()
        else:
            print("main:", self.__pMain.cache, "\nlocais:", self.__pCliente.cache, "\n", self.__pProduto.cache)


    def abre_tela(self):
        lista_opçoes = {1: self.tela_cliente, 2: self.tela_produtos, 3: self.tela_carrinho, 4: self.dev,
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

    @property
    def pProduto(self):
        return self.__pProduto

    @property
    def pCliente(self):
        return self.__pCliente