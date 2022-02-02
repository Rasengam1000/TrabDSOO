from ControladorPrincipal import ControladorPrinciapl
from TelaClientes import TelaClientes

class ControladorClientes:

    def __init__(self, controladorprincipal: ControladorPrincipal):
        self.__controladorprincipal = controladorprincipal
        self.__telaclientes = TelaClientes(self)
        self.__clientes = []

    def incluir_cliente(self):
        pass

    def excluir_cliente(self):
        pass



