import pickle
from abc import ABC, abstractmethod


class Pabstrato(ABC):
    def __init__(self, persistenciamain):
        self.__main = persistenciamain
        self.__cache = []

        try:
            self.abrir()
        except:
            self.guardar()

    @property
    def cache(self):
        return self.__cache

    @property
    def main(self):
        return self.__main
        
    @property
    def guardar(self):
        return self.__guardar
    
    @property
    def abrir(self):
        return self.__abrir


    def __guardar(self, tipo):                       #guarda na lista principal e grava no disco
        self.__main.guardar([tipo, self.__cache])

    def __abrir(self, tipo):
        self.__cache = self.__main.abrir(tipo)
    

    def add(self, objeto):                           #deixa no cache local e manda guardar na principal
        self.__cache.append(objeto)
        self.guardar()
    
    def remove(self, objeto):
        self.__cache.remove(objeto)
        self.guardar()

    def apagar(self):
        self.__cache = []
        self.guardar()
