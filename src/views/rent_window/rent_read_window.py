from customtkinter import *
from src.views.base_structures.basic_components import BasicComponents

class RentReadWindow(BasicComponents):
    def __init__(self, master):
        self._master = master
        super().__init__(self._master)
        self.labels()
        self.textEntries()
        self.sendButton()
        self.textBox()
        
    def labels(self):
        super().labels()
        self.txt1.configure(text='Listar Aluguel')
        self.txt2.configure(text='Código')

    def textEntries(self):
        super().textEntries()

    def sendButton(self):
        super().sendButton()
    
    def textBox(self):
        super().textBox()
