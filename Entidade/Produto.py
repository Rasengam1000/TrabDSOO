class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.__codigo = int(codigo.strip())
        self.__nome = str(nome).title().strip()
        self.__preco = float(preco)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = int(codigo)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = str(nome)

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = float(preco)