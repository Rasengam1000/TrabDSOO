from entidade.Carrinho import Carrinho

class Cliente:

    def __init__(self, nome: str, sobrenome: str, cpf: int, idade: int, tipo_cliente: str):
        self.__nome = nome.title()
        self.__sobrenome = sobrenome.title()
        self.__cpf = cpf
        self.__idade = idade
        self.__carrinho = Carrinho()
        self.__tipo_cliente = tipo_cliente.upper()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome: str):
        self.__sobrenome = sobrenome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @property
    def tipo_cliente(self):
        return self.__tipo_cliente

    @tipo_cliente.setter
    def tipo_cliente(self, tipo_cliente: str):
        self.__tipo_cliente = tipo_cliente

    @property
    def carrinho(self):
        return self.__carrinho