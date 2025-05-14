from customtkinter import *

class VehicleCreateWindow():
    def __init__(self, master):
        self.__master = master
        self.labels()
        self.textEntries()
        self.submitButton()
  
    def labels(self):
        self.txt1 = CTkLabel(self.__master, text='Adicionar Veículo', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)

        self.txt2 = CTkLabel(self.__master, text='Código', text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.05, rely=0.14, relwidth=0.2, relheight=0.07)
        
        self.txt3 = CTkLabel(self.__master, text='Categoria', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.47, rely=0.14, relwidth=0.2, relheight=0.07)

        self.txt4 = CTkLabel(self.__master, text='Combustível', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.07, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt5 = CTkLabel(self.__master, text='Ano', text_color='#808080', font=('', 14), justify='left')
        self.txt5.place(relx=0.45, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt6 = CTkLabel(self.__master, text='Modelo', text_color='#808080', font=('', 14), justify='left')
        self.txt6.place(relx=0.21, rely=0.59, relwidth=0.2, relheight=0.07)

    def textEntries(self): 
        self.code_entry = CTkEntry(self.__master, fg_color='#1C1C1C', font=('', 14))
        self.code_entry.place(relx=0.08, rely=0.2, relwidth=0.40, relheight=0.09)
      
        self.cat_entry = CTkEntry(self.__master, fg_color='#1C1C1C', font=('', 14))
        self.cat_entry.place(relx=0.50, rely=0.2, relwidth=0.40, relheight=0.09)

        self.fuel_entry = CTkEntry(self.__master, fg_color='#1C1C1C', font=('', 14))
        self.fuel_entry.place(relx=0.08, rely=0.43, relwidth=0.40, relheight=0.09)
      
        self.year_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.year_entry.place(relx=0.50, rely=0.43, relwidth=0.40, relheight=0.09)

        self.model_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.model_entry.place(relx=0.24, rely=0.65, relwidth=0.5, relheight=0.09)


    def textBox(self):
        pass #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.vehicle_submit_button = CTkButton(self.__master,corner_radius=100, text='ADICIONAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.vehicle_submit_button.place(relx=0.39, rely=0.85, relwidth=0.2, relheight=0.09)
