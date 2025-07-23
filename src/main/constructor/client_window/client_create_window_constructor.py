from src.views.client_window.client_create_window import ClientCreateWindow
from src.controllers.client_controllers.client_create_controller import ClientCreateController

class ClientCreateWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = ClientCreateWindow(self.right_frame)
        self.controller = ClientCreateController()
        self.button_command()
    
    def get_client_data(self) -> dict:
        cpf = self.create_window.cpf_entry.get()
        name = self.create_window.name_entry.get()
        adress = self.create_window.adress_entry.get()
        phone_number = self.create_window.fone_entry.get()
        
        data_dict = {
            'cpf': cpf,
            'name': name,
            'adress': adress,
            'phone_number': phone_number
        }

        return data_dict


    def creating_client(self):
        data = self.get_client_data()
        try:
            message = self.controller.creating_client(data)
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
        self.create_window.name_entry.delete(0, "end")
        self.create_window.adress_entry.delete(0, "end")
        self.create_window.fone_entry.delete(0, "end")

    def button_command(self):
        self.create_window.client_submit_button.configure(command=self.creating_client)

    

    


    

    