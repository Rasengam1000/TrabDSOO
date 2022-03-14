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
                    [sg.Button("Listar\nCompras", key=3, size=(10,5)), sg.Button("Pagamento", key=4, size=(10,5))],
                    [sg.Button("Voltar", key=0)]
        ]


        self.__mainwindow = sg.Window("Tela Carrinho", default_element_size=()).Layout(layout)


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

    def mostrar_info(self, carrinho_mostrar):
        info = [
                    [sg.Text("Carrinho:")],
                    [sg.Listbox(values=(carrinho_mostrar), size=(30, len(carrinho_mostrar)))],
                    [sg.Button("Voltar", key=0)]
        ]

        self.__infowindow = sg.Window("Info Carrinho").Layout(info)

        return self.__infowindow.Read()

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
        print(f"".ljust(39,"-"))

        for linha in extrato:         #imprime o extrato
            print(f"| {linha:35} |")

        print(f"".ljust(39,"-"))


        print("\033[1;38;2;0;150;0m" f"\nTotal: R$ {total}" "\033[0m")
