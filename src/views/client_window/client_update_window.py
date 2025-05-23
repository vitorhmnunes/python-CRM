from customtkinter import *
from src.views.base_structures.basic_components import BasicComponents

class ClientUpdateWindow(BasicComponents):
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
        self.txt1.configure(text='Alterar Cliente')
        self.txt2.configure(text='CPF')

    def textEntries(self):
        super().textEntries()
        self.primary_key_entry.configure(placeholder_text='(000.000.000-00)')

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

    
#Window to insert the new client informations
class UpdateInfosToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color = '#272727', **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title('Alterar Cliente')
        self.geometry('600x500')
        self.resizable(False,False)
        self.labels()
        self.textEntries()
        self.submitButton()
  
    def labels(self):
        self.txt1 = CTkLabel(self, text='Alterar Cliente', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
      
        self.txt2 = CTkLabel(self, text='Nome', text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.05, rely=0.14, relwidth=0.3, relheight=0.07)
        
        self.txt3 = CTkLabel(self, text='Endereço', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.07, rely=0.33, relwidth=0.3, relheight=0.07)
       
        self.txt4 = CTkLabel(self, text='Telefone', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.11, rely=0.54, relwidth=0.21, relheight=0.07)

    def textEntries(self): 
        self.name_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.name_entry.place(relx=0.15, rely=0.21, relwidth=0.7, relheight=0.09)
      
        self.adress_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.adress_entry.place(relx=0.15, rely=0.41, relwidth=0.7, relheight=0.09)
  
        self.phone_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='(00) 00000-0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.phone_entry.place(relx=0.15, rely=0.61, relwidth=0.7, relheight=0.09)
      

    def textBox(self):
        pass #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.update_submit_button = CTkButton(self,corner_radius=100, text='ALTERAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.update_submit_button.place(relx=0.28, rely=0.85, relwidth=0.2, relheight=0.09)

        self.cancel_button = CTkButton(self,corner_radius=100, text='CANCELAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969', command=self.cancelBtCallback)
        self.cancel_button.place(relx=0.5, rely=0.85, relwidth=0.2, relheight=0.09)

    def cancelBtCallback(self):
        self.withdraw()
    