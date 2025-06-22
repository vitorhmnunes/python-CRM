from customtkinter import CTkButton

#upper menu buttons to go to client, vehicle and rent windows
class UpperMenuButtons():
    def __init__(self, master):
        self._master = master
        self.insertButtons()

    def clientButton(self):
        self.client_bt = CTkButton(self._master, corner_radius=0, text='Clientes', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.client_bt.place(relx=0.002, rely=0.1, relwidth=0.1, relheight=0.7)

    def vehicleButton(self):
        self.vehicle_bt = CTkButton(self._master, corner_radius=0, text='Veículos', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.vehicle_bt.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.7)

    def rentButton(self):
        self.rent_bt = CTkButton(self._master, corner_radius=0, text='Alugueis', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.rent_bt.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.7)

    def insertButtons(self):
        self.clientButton()
        self.vehicleButton()
        self.rentButton()