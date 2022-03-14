import PySimpleGUI as sg
import time

from Limite.AbstractTela import AbstractTela
from Limite.CaracteresNumericosException import CaracteresNumericosException


class TelaProdutos:
    def __init__(self):
        self.__mainwindow = None
        self.__getinfowindow = None
        self.__infowindow = None
        self.__selecionarwindow = None
        self.init_tela() 


    @property
    def mainwindow(self):
        if self.__mainwindow != None:
            return self.__mainwindow


    def init_tela(self):
        sg.ChangeLookAndFeel("Reddit")
        layout = [
                    [sg.Button("Inserir\nProduto", key=1, size=(10,5)), sg.Button("Excluir\nProduto", key=2, size=(10,5)), sg.Button("Listar\nProdutos", key=3, size=(10,5))],
                    [sg.Button("Voltar", key=0)]
        ]


        self.__mainwindow = sg.Window("Tela Produtos", default_element_size=()).Layout(layout)


    def opcoes(self):
        self.init_tela() 
        return self.__mainwindow.read()

    def close(self):
        self.__mainwindow.close()

    def close_getinfo(self):
        self.__getinfowindow.close()

    def close_info(self):
        self.__infowindow.close()

    def close_selecionarwindow(self):
        self.__selecionarwindow.Close()

    def pegar_info(self):
        info = [
                    [sg.Text("Qual o código, nome e preço do produto que deseja registrar?")],
                    [sg.Text("Código"), sg.InputText()],
                    [sg.Text("Nome"), sg.InputText()],
                    [sg.Text("Preço"), sg.InputText()],
                    [sg.Button("Voltar", key=0), sg.Button("Enviar")]
        ]


        self.__getinfowindow = sg.Window("Inserir Produto").Layout(info)

        while True:
            read = self.__getinfowindow.read()
            botao = read[0]
            valores = read[1]

            if botao == "00":
                break
            codigo = valores[0][0]
            preço = valores[0][2]
            try:
                if not codigo.isnumeric() or not codigo.isnumeric():
                    raise CaracteresNumericosException

            except CaracteresNumericosException:
                self.printar("Código e preço devem ser numéricos")
            else:
                break

        return read
            

    def printar(self, mensagem):
        sg.Popup(mensagem)

    def mostrar_info(self, produtos_mostrar):
        info = [
                    [sg.Table(values=produtos_mostrar, headings=["Código", "Nome do Produto", "Preço"],
                                auto_size_columns=True,
                                justification='left',
                                num_rows=15,
                                alternating_row_color='lightblue',)],
                    [sg.Button("Voltar", key=0)]
        ]

        self.__infowindow = sg.Window("Info Produtos").Layout(info)

        return self.__infowindow.read()

    def selecionar_produto(self, produtos_mostrar):
        info = [
                    [sg.Text("Selecione o Produto")],
                    [sg.Listbox(values=(produtos_mostrar), size=(30, 15))],
                    [sg.Button("Selecionar", key=1)],
                    [sg.Button("Voltar", key=0)]
        ]

        self.__selecionarwindow = sg.Window("Produtos").Layout(info)


        return self.__selecionarwindow.read()

