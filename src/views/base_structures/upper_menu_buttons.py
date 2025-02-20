from customtkinter import CTkButton

#upper menu buttons to go to client, vehicle and rent windows
class UpperMenuButtons():
    def __init__(self, master) -> None:
        self.__master = master
        self.insertButtons()

    def clientButton(self) -> None:
        self.client_bt = CTkButton(self.__master, corner_radius=0, text='Clientes', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.client_bt.place(relx=0.002, rely=0.1, relwidth=0.1, relheight=0.7)

    def vehicleButton(self) -> None:
        self.vehicle_bt = CTkButton(self.__master, corner_radius=0, text='Veículos', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.vehicle_bt.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.7)

    def rentButton(self) -> None:
        self.rent_bt = CTkButton(self.__master, corner_radius=0, text='Alugueis', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.rent_bt.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.7)

    def insertButtons(self) -> None:
        self.clientButton()
        self.vehicleButton()
        self.rentButton()