from customtkinter import *
from src.views.base_structures.basic_components import BasicComponents
from src.views.base_structures.alert_window import AlertWindow

class VehicleDeleteWindow(BasicComponents):
    def __init__(self, master):
        self._master = master
        super().__init__(self._master)
        self.labels()
        self.textEntries()
        self.sendButton()
        self.textBox()
        self.confirmButton()
        
    def labels(self):
        super().labels()
        self.txt1.configure(text='Listar Veículo')
        self.txt2.configure(text='Código')

    def textEntries(self):
        super().textEntries()

    def sendButton(self):
        super().sendButton()
    
    def textBox(self):
        super().textBox()

    def alertWindowCall(self):
        self.alert_window = AlertWindow()

    def confirmButton(self):
        super().confirmButton()
        self.confirm_bt.configure(text='EXCLUIR')
        self.confirm_bt.configure(command=self.alertWindowCall)