from abc import ABC, abstractmethod
from Persistencia.DataSource import DataSource


class DAOabstrato(ABC):
    @abstractmethod
    def __init__(self, key):
        self.__main = DataSource()
        self.__cache = []
        self.__abrir(key)


    @property
    def cache(self):
        return self.__cache

    @property
    def main(self):
        return self.__main

    @property
    def guardar(self):
        return self.__guardar

    def __guardar(self, tipo):                       #guarda na lista principal e grava no disco
        print(self.__cache)
        self.__main.guardar([tipo, self.__cache])

    def __abrir(self, tipo):
        self.__cache = self.__main.abrir(tipo)
    
    def add(self, objeto, key):                           #deixa no cache local e manda guardar na principal
        self.__cache.append(objeto)
        self.__guardar(key)
    
    def remove(self, objeto, key):
        self.__cache.remove(objeto)
        self.__guardar(key)

    def apagar(self, key):         
        self.__cache = []
        self.__guardar(key)
