from Limite.AbstractTela import AbstractTela
import PySimpleGUI as sg

class TelaClientes(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('escolha as opções')],
            [sg.Button('Incluir Cliente', key=1)],
            [sg.Button('Excluir Cliente', key=2)],
            [sg.Button('Alterar Cadastro', key=3)],
            [sg.Button('Informacao Cliente', key=4)],
            [sg.Button('Listar Clientes', key=5)],
            [sg.Button('Voltar', key=0)]
        ]
        self.__window = sg.Window('Clientes').Layout(layout)

    def opcoes(self):
        button, values = self.__window.Read()
        if button is None:
            button = 0
        return button

    def close(self):
        self.__window.Close()
        self.init_components()