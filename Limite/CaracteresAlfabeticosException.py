class CaracteresAlfabeticosException(Exception):

    def __init__(self):
        frase = 'As opções nome e sobrenome só aceitam letras'
        super().__init__(frase)