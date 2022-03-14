from abc import ABC, abstractmethod
import PySimpleGUI as sg

class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def show_message(self, titulo, mensagem):
        sg.Popup(titulo, mensagem)

