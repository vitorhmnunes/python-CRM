from customtkinter import *
from src.views.base_structures.base_frame import BaseFrame
from src.views.base_structures.base_frame import RightFrame
from src.views.vehicle_window.vehicle_create_window import VehicleCreateWindow

class VehicleBaseWindow():
    def __init__(self, root):
        self.root = root
        self.frame = BaseFrame(root)
        self.leftFrameLabel(self.frame.left_corner_frame)
        self.createVehicle()

    def leftFrameLabel(self, left_corner_frame):
        self.left_label = CTkLabel(left_corner_frame, text="Veículos" , text_color='#2F4F4F', font=('impact', 50), justify='left' )
        self.left_label.place(relx=0.12, rely=0.2, relwidth=0.6, relheight=0.15)

    def createVehicle(self):
        self.right_frame = RightFrame(self.root)
        self.creat_client_window = VehicleCreateWindow(self.right_frame) 
    
    def newRightFrame(self):
        self.new_frame = RightFrame(self.root)