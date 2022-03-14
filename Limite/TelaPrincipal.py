from Limite.AbstractTela import AbstractTela
import PySimpleGUI as sg


class TelaPrincipal(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Escolha as opções')],
            [sg.Button('Clientes', key=1)],
            [sg.Button('Produtos', key=2)],
            [sg.Button('Carrinho', key=3)],
            [sg.Button('Sair', key=0)]
                ]
        self.__window = sg.Window('Balada').Layout(layout)

    def opcoes(self):
        button, values = self.__window.Read()
        if button is None:
            button = 0
        return button

    def close(self):
        self.__window.Close()
        self.init_components()