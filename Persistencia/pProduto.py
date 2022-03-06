import pickle
from Persistencia.pAbstrato import Pabstrato
from Entidade.Produto import Produto


class Pproduto(Pabstrato):
    def __init__(self, persistenciamain):
        super().__init__(persistenciamain)

    def guardar(self):
        super().guardar("produtos")

    def abrir(self):
        super().abrir("produtos")

    def add(self, objeto: Produto):
        if objeto != None and isinstance(objeto, Produto):
            super().add(objeto)

    def remove(self, objeto: Produto):
        if objeto != None and isinstance(objeto, Produto):
            super().remove(objeto)
