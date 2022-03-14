import pickle
from pathlib import Path

#Classe persistencia principal, criada com a intenção de ter apenas 1 arquivo persistente, contento os caches
#das outras 2 classes persistentes. As outras classes usam os metodos aqui para guardar e abrir.
#Essas outras classes tem seu proprio cache (uma copia atualizada da sua parte vinda do cache daqui).


class DataSource:
    __instance = None       
    def __init__(self):
        self.__arquivo = f"{Path.home()}\Documents\pBalada.pkl"     #universializar path para o user (mudar?)
        self.__cache = {"clientes":[], "produtos":[]}

        try:
            self.__abrir()
        except:
            self.__guardar()


    @property
    def cache(self):
        return self.__cache

    @property
    def guardar(self):
        return self.__guardar

    @property
    def abrir(self):
        return self.__abrir

    def __new__(cls):                                   
        if DataSource.__instance is None:
            DataSource.__instance = object.__new__(cls)
        return DataSource.__instance


    def __guardar(self, data=None):
        if data != None:
            self.__cache[data[0]] = data[1]
            pickle.dump(self.__cache, open(self.__arquivo, "wb"))
            
        else:
            pickle.dump(self.__cache, open(self.__arquivo, "wb"))

    def __abrir(self, data=None):
        if data != None:
            self.__cache = pickle.load(open(self.__arquivo, "rb"))
            return self.__cache[data]
        else:
            self.__cache = pickle.load(open(self.__arquivo, "rb"))


    def apagar(self):
        self.__cache = {"clientes":[], "produtos":[]}
        pickle.dump(self.__cache, open(self.__arquivo, "wb"))
