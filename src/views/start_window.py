from customtkinter import *
from src.views.base_structures.base_frame import BaseFrame, UpperFrame

class StartWindow():
    def __init__(self, root):
        self.frame = BaseFrame(root)
        self.upper_frame = UpperFrame(root)
        self.leftFrameLabel(self.frame.left_corner_frame)
        self.centralFrameLabels(self.frame)
        self.centralTextEntries(self.frame)
        self.centralEntriesButtons(self.frame)
        self.centralTextboxes(self.frame)

    def leftFrameLabel(self, left_frame) -> None:
        self.text = CTkLabel(left_frame, text='Car\nRental\nInterface', text_color='#2F4F4F', font=('impact', 50), justify='left')
        self.text.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.5)

    def centralFrameLabels(self, right_frame) -> None:
        self.text1 = CTkLabel(right_frame, text='Acesso Rápido', text_color='#808080', font=('', 18), justify='left')
        self.text1.place(relx=0.33, rely=0.07, relwidth=0.2, relheight=0.07)

        self.text2 = CTkLabel(right_frame, text='Cliente', text_color='#808080', font=('', 14), justify='left')
        self.text2.place(relx=0.36, rely=0.13, relwidth=0.1, relheight=0.07)

        self.text3 = CTkLabel(right_frame, text='Alugueis', text_color='#808080', font=('', 14), justify='left')
        self.text3.place(relx=0.36, rely=0.5, relwidth=0.1, relheight=0.07)

        self.text4 = CTkLabel(right_frame, text='ou', text_color='#808080', font=('', 14), justify='center')
        self.text4.place(relx=0.632, rely=0.57, relwidth=0.1, relheight=0.07) 

    def centralTextEntries(self, right_frame) -> None:
        self.cpf_entry = CTkEntry(right_frame, fg_color='#1C1C1C', placeholder_text='CPF (000.000.000-00)', placeholder_text_color='#FFFFFF', font=('', 14))
        self.cpf_entry.place(relx=0.40, rely=0.2, relwidth=0.37, relheight=0.06)

        self.rent_code_entry = CTkEntry(right_frame, fg_color='#1C1C1C', placeholder_text='Código do aluguel', placeholder_text_color='#FFFFFF', font=('', 14))
        self.rent_code_entry.place(relx=0.40, rely=0.57, relwidth=0.2, relheight=0.06)

        self.vehicle_code_entry = CTkEntry(right_frame, fg_color='#1C1C1C', placeholder_text='Código do veículo', placeholder_text_color='#FFFFFF', font=('', 14))
        self.vehicle_code_entry.place(relx=0.71, rely=0.57, relwidth=0.2, relheight=0.06)

    def centralEntriesButtons(self,right_frame) -> None:
        self.cpf_search_button = CTkButton(right_frame, corner_radius=5, text='IR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.cpf_search_button.place(relx=0.78, rely=0.2, relwidth=0.1, relheight=0.06)

        self.rent_code_button = CTkButton(right_frame, corner_radius=5, text='IR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.rent_code_button.place(relx=0.61, rely=0.57, relwidth=0.05, relheight=0.06)

        self.vehicle_code_button = CTkButton(right_frame, corner_radius=5, text='IR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.vehicle_code_button.place(relx=0.92, rely=0.57, relwidth=0.05, relheight=0.06)

    def centralTextboxes(self, right_frame) -> None:
        self.client_tb = CTkTextbox(right_frame, corner_radius=5, fg_color='#1C1C1C', text_color='#FFFFFF', scrollbar_button_color='#FFFFFF', scrollbar_button_hover_color='#FFFFFF', font=('', 12), state='disabled', border_width=2 )
        self.client_tb.place(relx=0.36, rely=0.28, relwidth=0.6, relheight=0.2)

        self.rent_tb = CTkTextbox(right_frame, corner_radius=5, fg_color='#1C1C1C', text_color='#FFFFFF', scrollbar_button_color='#FFFFFF', scrollbar_button_hover_color='#FFFFFF', font=('', 12), state='disabled', border_width=2 )
        self.rent_tb.place(relx=0.36, rely=0.66, relwidth=0.6, relheight=0.26)