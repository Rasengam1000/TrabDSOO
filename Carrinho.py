class Carrinho:
    def __init__(self):
        self.__compras = []
        self.__extrato = []


    @property
    def compras(self):
        return self.__compras

    @property
    def extrato(self):
        return self.__extrato
