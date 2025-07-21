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

    def confirmButton(self):
        super().confirmButton()
        self.confirm_bt.configure(text='ALTERAR')


class UpdateInfosToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color = '#272727', **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title('Alterar Veículo')
        self.geometry('600x500')
        self.resizable(False,False)
        self.labels()
        self.textEntries()
        self.submitButton()
        self.textBox()
    
    def labels(self):
        self.txt1 = CTkLabel(self, text='Alterar Aluguel', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
      
        self.txt2 = CTkLabel(self, text='Código Veículo', text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.09, rely=0.14, relwidth=0.3, relheight=0.07)
        
        self.txt3 = CTkLabel(self, text='Data Inicial', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.07, rely=0.33, relwidth=0.3, relheight=0.07)
       
        self.txt4 = CTkLabel(self, text='Data Final', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.11, rely=0.54, relwidth=0.21, relheight=0.07)

    def textEntries(self): 
        self.vehicle_code_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.vehicle_code_entry.place(relx=0.15, rely=0.21, relwidth=0.7, relheight=0.09)
      
        self.inicial_date_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.inicial_date_entry.place(relx=0.15, rely=0.41, relwidth=0.7, relheight=0.09)
  
        self.final_date_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.final_date_entry.place(relx=0.15, rely=0.61, relwidth=0.7, relheight=0.09)
      
    def textBox(self):
        self.text_box = CTkTextbox(self, fg_color='#272727', border_spacing=0, border_color='#272727', border_width=0, state="disabled")
        self.text_box.place(relx=0.4, rely=0.01, relwidth=0.6, relheight=0.13) #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.update_submit_button = CTkButton(self,corner_radius=100, text='ALTERAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.update_submit_button.place(relx=0.28, rely=0.85, relwidth=0.2, relheight=0.09)

        self.cancel_button = CTkButton(self,corner_radius=100, text='CANCELAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969', command=self.cancelBtCallback)
        self.cancel_button.place(relx=0.5, rely=0.85, relwidth=0.2, relheight=0.09)

    def cancelBtCallback(self):
        self.withdraw()