from src.views.client_window.client_read_window import ClientReadWindow
from src.controllers.client_controllers.client_read_controller import ClientReadController

class ClientReadWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.read_window = ClientReadWindow(self.master)
        self.controller = ClientReadController()
        self.button_command()

    def get_client_cpf(self):
        cpf = self.read_window.primary_key_entry.get()
        return cpf

    def formating_db_return(self, dict_list):
        values_list = list(dict_list[0].values())
        message = f"CPF: {values_list[0]} || Name: {values_list[1]}\nAdress: {values_list[2]} || Phone Number: {values_list[3]}\n"
        return message

    def reading_client(self):
        cpf = self.get_client_cpf()
        try:
            message = self.controller.reading_client(cpf)
            values_string = self.formating_db_return(message)
            self.read_window.tb.configure(state="normal", text_color='white')
            self.read_window.tb.delete("1.0", "end")
            self.read_window.tb.insert(index='0.0', text=values_string)
            self.read_window.tb.configure(state="disabled")
        except Exception as err:
            self.read_window.tb.configure(state="normal", text_color="red")
            self.read_window.tb.delete("1.0", "end")
            self.read_window.tb.insert(index='0.0', text=err)
            self.read_window.tb.configure(state="disabled")

    def button_command(self):
        self.read_window.send_bt.configure(command=self.reading_client)
    