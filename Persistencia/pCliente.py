import pickle
from Persistencia.pAbstrato import Pabstrato
from Entidade.Cliente import Cliente


class Pcliente(Pabstrato):
    def __init__(self, persistenciamain):
        super().__init__(persistenciamain)

    def guardar(self):
        super().guardar("clientes")

    def abrir(self):
        super().abrir("clientes")

    def add(self, objeto: Cliente):
        if objeto != None and isinstance(objeto, Cliente):
            super().add(objeto)

    def remove(self, objeto: Cliente):
        if objeto != None and isinstance(objeto, Cliente):
            super().remove(objeto)
