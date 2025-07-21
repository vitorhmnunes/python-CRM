from customtkinter import *

class RentCreateWindow():
    def __init__(self, master):
        self._master = master
        self.labels()
        self.textEntries()
        self.submitButton()
        self.textBox()
  
    def labels(self):
        self.txt1 = CTkLabel(self._master, text='Adicionar Aluguel', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
        
        self.txt2 = CTkLabel(self._master, text='CPF', text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.19, rely=0.14, relwidth=0.2, relheight=0.07)

        self.txt3 = CTkLabel(self._master, text='Código Veículo', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.08, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt4 = CTkLabel(self._master, text='Data Inical', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.47, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt5 = CTkLabel(self._master, text='Data Final', text_color='#808080', font=('', 14), justify='left')
        self.txt5.place(relx=0.21, rely=0.59, relwidth=0.2, relheight=0.07)

    def textEntries(self): 
        self.cpf_entry = CTkEntry(self._master, fg_color='#1C1C1C', placeholder_text='000.000.000-00', placeholder_text_color='#FFFFFF', font=('', 14))
        self.cpf_entry.place(relx=0.24, rely=0.2, relwidth=0.5, relheight=0.09)

        self.vehicle_code_entry = CTkEntry(self._master, fg_color='#1C1C1C', font=('', 14))
        self.vehicle_code_entry.place(relx=0.08, rely=0.43, relwidth=0.40, relheight=0.09)
      
        self.inicial_date_entry = CTkEntry(self._master, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.inicial_date_entry.place(relx=0.50, rely=0.43, relwidth=0.40, relheight=0.09)

        self.final_date_entry = CTkEntry(self._master, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.final_date_entry.place(relx=0.24, rely=0.65, relwidth=0.5, relheight=0.09)

    def textBox(self):
        self.text_box = CTkTextbox(self._master, fg_color='#272727', border_spacing=0, border_color='#272727', border_width=0, state='disabled')
        self.text_box.place(relx=0.4, rely=0.01, relwidth=0.6, relheight=0.13) 

    def submitButton(self):
        self.rent_submit_button = CTkButton(self._master,corner_radius=100, text='ADICIONAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.rent_submit_button.place(relx=0.39, rely=0.85, relwidth=0.2, relheight=0.09)