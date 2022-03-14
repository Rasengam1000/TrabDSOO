from Limite.AbstractTela import AbstractTela
import PySimpleGUI as sg


class TelaClientesCpf(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('CPF do cliente desejado'), sg.InputText('cpf', key='cpf')],
            [sg.Button('Gravar', key='salvar'), sg.Button('Cancelar', key='sair')]
        ]
        self.__window = sg.Window('coleta cpfs').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
        self.init_components()