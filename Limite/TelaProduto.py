import PySimpleGUI as sg
from Limite.AbstractTela import AbstractTela
import time
#testar table
#https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Table_Element.py


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

        return self.__getinfowindow.Read()


    def printar(self, mensagem):
        sg.Popup(mensagem)

    def mostrar_info(self, produtos_mostrar):
        info = [
                    [sg.Text("Produtos Disponíveis")],
                    [sg.Listbox(values=(produtos_mostrar), size=(30, len(produtos_mostrar)))],
                    [sg.Button("Voltar", key=0)]
        ]

        self.__infowindow = sg.Window("Info Produtos").Layout(info)

        return self.__infowindow.Read()

    def selecionar_produto(self, produtos_mostrar):
        info = [
                    [sg.Text("Selecione o Produto")],
                    [sg.Listbox(values=(produtos_mostrar), size=(30, len(produtos_mostrar)))],
                    [sg.Button("Selecionar", key=1)],
                    [sg.Button("Voltar", key=0)]
        ]

        self.__selecionarwindow = sg.Window("Produtos").Layout(info)

        return self.__selecionarwindow.Read()

