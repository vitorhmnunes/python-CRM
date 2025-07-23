from src.views.vehicle_window.vehicle_create_window import VehicleCreateWindow
from src.controllers.vehicle_controllers.vehicle_create_controller import VehicleCreateController

class VehicleCreateWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = VehicleCreateWindow(self.right_frame)
        self.controller = VehicleCreateController()
        self.button_command()
    
    def get_vehicle_data(self) -> dict:
        code = self.create_window.code_entry.get()
        category = self.create_window.cat_entry.get()
        fuel = self.create_window.fuel_entry.get()
        year = self.create_window.year_entry.get()
        model = self.create_window.model_entry.get()
        
        data_dict = {
            'code': code,
            'category': category,
            'fuel': fuel,
            'year': year,
            'model': model
        }

        return data_dict


    def creating_vehicle(self):
        data = self.get_vehicle_data()
        try:
            message = self.controller.creating_vehicle(data)
            self.create_window.text_box.configure(state="normal", text_color="green")
            self.create_window.text_box.delete("1.0", "end")
            self.create_window.text_box.insert(index='0.0', text=message)
            self.create_window.text_box.configure(state="disabled")
            self.delete_entries_data()
        except Exception as err:
            self.create_window.text_box.configure(state="normal", text_color="red")
            self.create_window.text_box.delete("1.0", "end")
            self.create_window.text_box.insert(index='0.0', text=err)
            self.create_window.text_box.configure(state="disabled")
    
    def delete_entries_data(self):
        self.create_window.code_entry.delete(0, "end")
        self.create_window.cat_entry.delete(0, "end")
        self.create_window.fuel_entry.delete(0, "end")
        self.create_window.year_entry.delete(0, "end")
        self.create_window.model_entry.delete(0, "end")

    def button_command(self):
        self.create_window.vehicle_submit_button.configure(command=self.creating_vehicle)