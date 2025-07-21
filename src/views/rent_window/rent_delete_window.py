from customtkinter import *
from src.views.base_structures.basic_components import BasicComponents

class RentDeleteWindow(BasicComponents):
    def __init__(self, master):
        super().__init__(master)
        self.labels()
        self.textEntries()
        self.sendButton()
        self.textBox()
        self.confirmButton()
        
    def labels(self):
        super().labels()
        self.txt1.configure(text='Excluir Aluguel')
        self.txt2.configure(text='Código')

    def textEntries(self):
        super().textEntries()

    def sendButton(self):
        super().sendButton()
    
    def textBox(self):
        super().textBox()
    
    def confirmButton(self):
        super().confirmButton()
        self.confirm_bt.configure(text='EXCLUIR')  