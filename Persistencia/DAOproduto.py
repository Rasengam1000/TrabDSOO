import pickle
from Persistencia.DAOabstrato import DAOabstrato
from Entidade.Produto import Produto


class DAOproduto(DAOabstrato):
    def __init__(self):
        super().__init__("produtos")


    def add(self, objeto: Produto):
        if objeto != None and isinstance(objeto, Produto):
            super().add(objeto, "produtos")

    def remove(self, objeto: Produto):
        if objeto != None and isinstance(objeto, Produto):
            super().remove(objeto, "produtos")
