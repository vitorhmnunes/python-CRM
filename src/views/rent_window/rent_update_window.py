from customtkinter import *
from src.views.base_structures.basic_components import BasicComponents

class RentUpdateWindow(BasicComponents):
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
        self.txt1.configure(text='Alterar Aluguel')
        self.txt2.configure(text='Código')

    def textEntries(self):
        super().textEntries()

    def sendButton(self):
        super().sendButton()
    
    def textBox(self):
        super().textBox()

    def infosWindowCall(self):
        self.update_infos = UpdateInfosToplevelWindow()

    def confirmButton(self):
        super().confirmButton()
        self.confirm_bt.configure(text='ALTERAR')
        self.confirm_bt.configure(command=self.infosWindowCall)


class UpdateInfosToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color = '#272727', **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title('Alterar Veículo')
        self.geometry('600x500')
        self.resizable(False,False)
        self.labels()
        self.textEntries()
        self.submitButton()
        self.labels()
        self.textEntries()
        self.submitButton()
  
    def labels(self):
        self.txt1 = CTkLabel(self, text='Alterar Aluguel', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
        
        self.txt3 = CTkLabel(self, text='CPF', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.18, rely=0.14, relwidth=0.2, relheight=0.07)

        self.txt4 = CTkLabel(self, text='Código Veículo', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.08, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt5 = CTkLabel(self, text='Data Inical', text_color='#808080', font=('', 14), justify='left')
        self.txt5.place(relx=0.47, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt6 = CTkLabel(self, text='Data Final', text_color='#808080', font=('', 14), justify='left')
        self.txt6.place(relx=0.21, rely=0.59, relwidth=0.2, relheight=0.07)

    def textEntries(self): 
        self.cpf_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.cpf_entry.place(relx=0.24, rely=0.2, relwidth=0.5, relheight=0.09)

        self.vehicle_code_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.vehicle_code_entry.place(relx=0.08, rely=0.43, relwidth=0.40, relheight=0.09)
      
        self.inicial_date_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.inicial_date_entry.place(relx=0.50, rely=0.43, relwidth=0.40, relheight=0.09)

        self.final_date_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.final_date_entry.place(relx=0.24, rely=0.65, relwidth=0.5, relheight=0.09)


    def textBox(self):
        pass #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.rent_submit_button = CTkButton(self,corner_radius=100, text='ALTERAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.rent_submit_button.place(relx=0.28, rely=0.85, relwidth=0.2, relheight=0.09)

        self.cancel_button = CTkButton(self,corner_radius=100, text='CANCELAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969', command=self.cancelBtCallback)
        self.cancel_button.place(relx=0.5, rely=0.85, relwidth=0.2, relheight=0.09)

    def cancelBtCallback(self):
        self.withdraw()