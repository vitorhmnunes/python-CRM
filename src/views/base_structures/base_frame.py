from customtkinter import CTkFrame

#base frame for all windows
class BaseFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=0, fg_color='#272727')
        self.place(relx=0, rely=0, relwidth= 1, relheight=1)
        self.frames()
    
    def frames(self):
        self.left_corner_frame = CTkFrame(self, corner_radius=0, fg_color='#1C1C1C', border_color='#000000', border_width=1)
        self.left_corner_frame.place(relx=0, rely=0, relwidth= 0.33, relheight=1 )

        self.upper_corner_frame = CTkFrame(self, corner_radius=0, fg_color='#1C1C1C', border_color='#000000', border_width=1 )
        self.upper_corner_frame.place(relx=0, rely=0, relwidth= 1, relheight=0.06 )

#frame for CRUD options for cliente, vehicle and rent
class RightFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=0, fg_color='#272727')
        self.place(relx=0.33, rely=0.06, relwidth= 0.66, relheight=0.94)