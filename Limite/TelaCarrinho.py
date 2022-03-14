import PySimpleGUI as sg
from Limite.AbstractTela import AbstractTela
import time
#testar table
#https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Table_Element.py


class TelaCarrinho:
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
                    [sg.Button("Incluir\nCompra", key=1, size=(10,5)), sg.Button("Excluir\nCompra", key=2, size=(10,5))],
                    [sg.Button("Pagamento", key=4, size=(10,5))],
                    [sg.Button("Voltar", key=0)]
        ]


        self.__mainwindow = sg.Window("Tela Carrinho", default_element_size=()).Layout(layout)


    def opcoes(self):
        self.init_tela() 
        return self.__mainwindow.read()

    def close(self):
        self.__mainwindow.close()

    def close_pagar(self):
        self.__pagar.close()

    def close_infowindow(self):
        self.__infowindow.close()

    def close_selecionarwindow(self):
        self.__selecionarwindow.Close()

    def close_getinfo(self):
        self.__getinfowindow.close()

    def pegar_resposta(self,msg):
        info = [
                    [sg.Text(msg), sg.InputText()],
                    [sg.Button("Voltar", key=0), sg.Button("Enviar")]
        ]

        self.__getinfowindow = sg.Window("Inserir Produto").Layout(info)

        return self.__getinfowindow.read()

    def selecionar_produto(self, carrinho_mostrar):
        info = [
                    [sg.Text("Selecione o produto para excluir do carrinho")],
                    [sg.Listbox(values=(carrinho_mostrar), size=(30, len(carrinho_mostrar)))],
                    [sg.Button("Selecionar", key=1)],
                    [sg.Button("Voltar", key=0)]
        ]

        self.__selecionarwindow = sg.Window("Excluir Produto").Layout(info)

        return self.__selecionarwindow.Read()

    def mostrar_extrato(self,extrato,total):
        info = [
                    [sg.Text("Extrato:")],
                    [sg.Table(values=extrato, headings=["Nome do Produto", "Preço"],
                                auto_size_columns=True,
                                justification='left',
                                num_rows=15,
                                alternating_row_color='lightblue',)],
                    [sg.Text(f"Total: {total}")],[sg.Button("Voltar", key=0)]
        ]

        self.__infowindow = sg.Window("Info Carrinho").Layout(info)

        return self.__infowindow.Read()

    def pagar(self,extrato,total):
        info = [
                    [sg.Text("Extrato:")],
                    [sg.Table(values=extrato, headings=["Nome do Produto", "Preço"],
                                auto_size_columns=True,
                                justification='left',
                                num_rows=15,
                                alternating_row_color='lightblue',)],
                    [sg.Text(f"Total: {total}")],
                    [sg.Button("Voltar", key=0), sg.Button("Pagar", key=1)]
        ]

        self.__infowindow = sg.Window("Info Carrinho").Layout(info)

        return self.__infowindow.Read()

    def printar(self, mensagem):
        sg.Popup(mensagem)