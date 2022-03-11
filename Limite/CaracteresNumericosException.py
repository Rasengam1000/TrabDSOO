class CaracteresNumericosException(Exception):

    def __init__(self):
        frase = 'As opções cpf e idade só aceitam números'
        super().__init__(frase)