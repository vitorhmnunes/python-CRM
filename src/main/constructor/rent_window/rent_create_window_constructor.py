from src.views.rent_window.rent_create_window import RentCreateWindow
from src.controllers.rent_controllers.rent_create_controller import RentCreateController

class RentCreateWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = RentCreateWindow(self.right_frame)
        self.controller = RentCreateController()
        self.button_command()

    def get_rent_data(self) -> dict:
        cpf = self.create_window.cpf_entry.get()
        vehicle_code = self.create_window.vehicle_code_entry.get()
        inicial_date = self.create_window.inicial_date_entry.get()
        final_date = self.create_window.final_date_entry.get()
        
        data_dict = {
            'cpf': cpf,
            'vehicle_code': vehicle_code,
            'inicial_date': inicial_date,
            'final_date': final_date
        }

        return data_dict
    
    def creating_rent(self):
        data = self.get_rent_data()
        try:
            message = self.controller.creating_rent(data)
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
        self.create_window.cpf_entry.delete(0, "end")
        self.create_window.vehicle_code_entry.delete(0, "end")
        self.create_window.inicial_date_entry.delete(0, "end")
        self.create_window.final_date_entry.delete(0, "end")

    def button_command(self):
        self.create_window.rent_submit_button.configure(command=self.creating_rent)