from customtkinter import CTkButton

# button to go back to start window
class GoBackButton():
    def __init__(self, master) -> None:
        self.master = master
    
    def goBackButton(self) -> None:
        self.go_back_button = CTkButton(master=self.master, text='<- VOLTAR', fg_color='#272727', text_color='#808080', font=('', 12), border_width=1, border_color='#000000')
        self.go_back_button.place(relx=0.7, rely=0.07, relwidth=0.25, relheight=0.05)   

  
