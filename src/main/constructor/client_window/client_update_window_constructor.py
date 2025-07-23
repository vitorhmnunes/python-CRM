from src.views.client_window.client_update_window import ClientUpdateWindow, UpdateInfosToplevelWindow
from src.controllers.client_controllers.client_read_controller import ClientReadController
from src.controllers.client_controllers.client_update_controller import ClientUpdateController

class ClientUpdateWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.update_window = ClientUpdateWindow(self.master)
        self.read_controller = ClientReadController()
        self.update_controller = ClientUpdateController()
        self.read_button_command()

    def get_client_cpf(self):
        cpf = self.update_window.primary_key_entry.get()
        return cpf

    def formating_db_return(self, dict_list):
        values_list = list(dict_list[0].values())
        message = f"CPF: {values_list[0]} || Name: {values_list[1]};\nAdress: {values_list[2]} || Phone Number: {values_list[3]}\n"
        return message

    def reading_client(self):
        self.cpf = self.get_client_cpf()
        try:
            message = self.read_controller.reading_client(self.cpf)
            values_string = self.formating_db_return(message)
            self.update_window.tb.configure(state="normal", text_color='white')
            self.update_window.tb.delete("1.0", "end")
            self.update_window.tb.insert(index='0.0', text=values_string)
            self.update_window.tb.configure(state="disabled")
            self.update_button_command()
        except Exception as err:
            self.update_window.tb.configure(state="normal", text_color="red")
            self.update_window.tb.delete("1.0", "end")
            self.update_window.tb.insert(index='0.0', text=err)
            self.update_window.tb.configure(state="disabled")

    def read_button_command(self):
        self.update_window.send_bt.configure(command=self.reading_client)

    def desable_update_bt(self):
        self.update_window.confirm_bt.configure(state="disabled")

    def clean_cpf_entry(self):
        self.update_window.primary_key_entry.delete(0, "end")

    def close_toplevel_window(self):
        self.toplevel_window.withdraw()

    def get_client_data(self) -> dict:
        cpf = self.cpf
        name = self.toplevel_window.name_entry.get()
        adress = self.toplevel_window.adress_entry.get()
        phone_number = self.toplevel_window.phone_entry.get()
        
        data_dict = {
            'cpf': cpf,
            'name': name,
            'adress': adress,
            'phone_number': phone_number
        }

        return data_dict

    def updating_client(self):
        client_data = self.get_client_data()
        try:
            message = self.update_controller.updating_client(client_data)
            self.update_window.tb.configure(state="normal", text_color='green')
            self.update_window.tb.delete("1.0", "end")
            self.update_window.tb.insert(index='0.0', text=message)
            self.update_window.tb.configure(state="disabled")
            self.close_toplevel_window()
        except Exception as err:
            self.toplevel_window.text_box.configure(state="normal", text_color="red")
            self.toplevel_window.text_box.delete("1.0", "end")
            self.toplevel_window.text_box.insert(index='0.0', text=err)
            self.toplevel_window.text_box.configure(state="disabled")
    
    def infos_window_call(self):
        self.toplevel_window = UpdateInfosToplevelWindow()
        self.toplevel_window.update_submit_button.configure(command=lambda: [self.updating_client(), self.desable_update_bt(), self.clean_cpf_entry()])

    def update_button_command(self):
        self.update_window.confirm_bt.configure(state='normal')
        self.update_window.confirm_bt.configure(command=self.infos_window_call)

    
    