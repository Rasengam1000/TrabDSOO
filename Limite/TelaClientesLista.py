from Limite.AbstractTela import AbstractTela
import PySimpleGUI as sg


class TelaClientesLista(AbstractTela):
    def __init__(self):
        self.__window = None

    def init_components(self, lista_clientes):
        sg.ChangeLookAndFeel('Reddit')
        headings = ['Nome', 'Sobrenome', 'CPF', 'Idade', '  Tipo  ']
        layout = [
            [sg.Table(values=lista_clientes, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightblue',)]
        ]
        self.__window = sg.Window('Informação Clientes').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        self.__window.Read()