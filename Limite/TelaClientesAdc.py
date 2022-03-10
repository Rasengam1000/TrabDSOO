from Limite.AbstractTela import AbstractTela
import PySimpleGUI as sg


class TelaClientesAdc(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.change_look_and_feel('Reddit')
        layout = [
            [sg.Text('Insira nome, sobrenome, cpf e idade')],
            [sg.Text('nome', size=(15, 1)), sg.InputText('nome', key='nome')],
            [sg.Text('sobrenome', size=(15, 1)), sg.InputText('sobrenome', key='sobrenome')],
            [sg.Text('CPF', size=(15, 1)), sg.InputText('CPF', key='cpf')],
            [sg.Text('idade', size=(15, 1)), sg.InputText('idade', key='idade')],
            [sg.Text('Tipo de Cliente'), sg.Radio('VIP', 'RD1', default=True, key='rd_opcao1'), sg.Radio('Comum', 'RD1', key='rd_opcao2')],
            [sg.Submit('Gravar', key='salvar'), sg.Cancel('Cancelar', key='sair')]
                ]
        self.__window = sg.Window('Cadastro de Clientes').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        if values['rd_opcao1'] is True:
            values['tipo_cliente'] = 'vip'
        else:
            values['tipo_cliente'] = 'comum'
        return button, values

    def close(self):
        self.__window.Close()
        self.init_components()