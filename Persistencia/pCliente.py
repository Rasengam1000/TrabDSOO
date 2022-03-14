import pickle
from Persistencia.DAOabstrato import DAOabstrato
from Entidade.Cliente import Cliente


class DAOcliente(DAOabstrato):
    def __init__(self):
        super().__init__("clientes")


    def atualizar_carrinho(self):
        super().guardar("clientes")

    def add(self, objeto: Cliente):
        if objeto != None and isinstance(objeto, Cliente):
            super().add(objeto, "clientes")

    def remove(self, objeto: Cliente):
        if objeto != None and isinstance(objeto, Cliente):
            super().remove(objeto, "clientes")
