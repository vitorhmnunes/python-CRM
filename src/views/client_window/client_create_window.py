from customtkinter import *

class ClientCreateWindow():
    def __init__(self, master):
        self.__master = master
        self.labels()
        self.textEntries()
        self.submitButton()
  
    def labels(self):
        self.txt1 = CTkLabel(self.__master, text='Adicionar Cliente', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
      
        self.txt2 = CTkLabel(self.__master, text='CPF', text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.07)
        
        self.txt3 = CTkLabel(self.__master, text='Nome', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.018, rely=0.27, relwidth=0.2, relheight=0.07)
       
        self.txt4 = CTkLabel(self.__master, text='Endereço', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.019, rely=0.45, relwidth=0.24, relheight=0.07)
        
        self.txt5 = CTkLabel(self.__master, text='Telefone', text_color='#808080', font=('', 14), justify='left')
        self.txt5.place(relx=0.015, rely=0.64, relwidth=0.24, relheight=0.07)

    def textEntries(self): 
        self.cpf_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='000.000.000-00', placeholder_text_color='#FFFFFF', font=('', 14))
        self.cpf_entry.place(relx=0.08, rely=0.17, relwidth=0.7, relheight=0.09)
      
        self.name_entry = CTkEntry(self.__master, fg_color='#1C1C1C', font=('', 14))
        self.name_entry.place(relx=0.08, rely=0.34, relwidth=0.7, relheight=0.09)
  
        self.adress_entry = CTkEntry(self.__master, fg_color='#1C1C1C', font=('', 14))
        self.adress_entry.place(relx=0.08, rely=0.53, relwidth=0.7, relheight=0.09)
      
        self.fone_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='(00)00000-0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.fone_entry.place(relx=0.08, rely=0.71, relwidth=0.7, relheight=0.09)

    def textBox(self):
        pass #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.client_submit_button = CTkButton(self.__master,corner_radius=100, text='ADICIONAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.client_submit_button.place(relx=0.37, rely=0.85, relwidth=0.2, relheight=0.09)