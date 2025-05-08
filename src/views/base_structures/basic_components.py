# base class with frame components, for READ, UPDATE and DELETE options in all objects windows

from customtkinter import *
from abc import ABC, abstractmethod


class BasicComponents(ABC):
    def __init__(self, master):
        self._master = master
    
    def labels(self):
        self.txt1 = CTkLabel(self._master, text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)

        self.txt2 = CTkLabel(self._master, text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.07)

        return self.txt1, self.txt2

    def textEntries(self):
        self.primary_key_entry = CTkEntry(self._master, fg_color='#1C1C1C', placeholder_text_color='#FFFFFF', font=('', 14))
        self.primary_key_entry.place(relx=0.08, rely=0.17, relwidth=0.7, relheight=0.09)

        return self.primary_key_entry

    def sendButton(self):
        self.send_bt = CTkButton(self._master, corner_radius=100, text='IR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.send_bt.place(relx=0.8, rely=0.18, relwidth=0.15, relheight=0.08)

        return self.send_bt

    def textBox(self):
        self.tb = CTkTextbox(self._master, corner_radius=5, fg_color='#1C1C1C', text_color='#FFFFFF', scrollbar_button_color='#FFFFFF', scrollbar_button_hover_color='#FFFFFF', font=('', 12), state='disabled', border_width=2 )
        self.tb.place(relx=0.08, rely=0.35, relwidth=0.8, relheight=0.4)

        return self.tb

    def confirmButton(self):
        self.confirm_bt = CTkButton(self._master, corner_radius=100, font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.confirm_bt.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.09)

        return self.confirm_bt