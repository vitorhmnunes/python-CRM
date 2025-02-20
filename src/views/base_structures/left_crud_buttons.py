from customtkinter import CTkButton

class LeftCrudButtons():
    def __init__(self, master) -> None:
        self.master = master
        self.insertButtons()

    def createButton(self) -> None:
        self.create_bt = CTkButton(self.master, corner_radius=500, text='ADICIONAR', font=('',14), fg_color='#272727', text_color='#808080', border_width=1, border_color='#000000')
        self.create_bt.place(relx=0.15, rely=0.37, relwidth=0.7, relheight=0.13)

    def readButton(self) -> None:
        self.read_bt = CTkButton(self.master, corner_radius=500, text='LISTAR', font=('',14), fg_color='#272727', text_color='#808080', border_width=1, border_color='#000000')
        self.read_bt.place(relx=0.15, rely=0.51, relwidth=0.7, relheight=0.13)

    def updateButton(self) -> None:
        self.update_bt = CTkButton(self.master, corner_radius=500, text='ALTERAR', font=('',14), fg_color='#272727', text_color='#808080', border_width=1, border_color='#000000')
        self.update_bt.place(relx=0.15, rely=0.65, relwidth=0.7, relheight=0.13)

    def deleteButton(self) -> None:
        self.delete_bt = CTkButton(self.master, corner_radius=500, text='EXCLUIR', font=('',14), fg_color='#272727', text_color='#808080', border_width=1, border_color='#000000')
        self.delete_bt.place(relx=0.15, rely=0.79, relwidth=0.7, relheight=0.13)

    def insertButtons(self) -> None:
        self.createButton()
        self.readButton()
        self.updateButton()
        self.deleteButton()
