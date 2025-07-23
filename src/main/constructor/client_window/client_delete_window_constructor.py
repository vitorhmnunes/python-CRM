from src.views.client_window.client_delete_window import ClientDeleteWindow
from src.views.base_structures.alert_window import AlertWindow
from src.controllers.client_controllers.client_delete_controller import ClientDeleteController
from src.controllers.client_controllers.client_read_controller import ClientReadController


class ClientDeleteWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.delete_window = ClientDeleteWindow(self.master)
        self.delete_controller = ClientDeleteController()
        self.read_controller = ClientReadController()
        self.read_button_command()

    def get_client_cpf(self):
        cpf = self.delete_window.primary_key_entry.get()
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
            self.delete_window.tb.configure(state="normal", text_color='white')
            self.delete_window.tb.delete("1.0", "end")
            self.delete_window.tb.insert(index='0.0', text=values_string)
            self.delete_window.tb.configure(state="disabled")
            self.delete_button_command()
        except Exception as err:
            self.delete_window.tb.configure(state="normal", text_color="red")
            self.delete_window.tb.delete("1.0", "end")
            self.delete_window.tb.insert(index='0.0', text=err)
            self.delete_window.tb.configure(state="disabled")

    def read_button_command(self):
        self.delete_window.send_bt.configure(command=self.reading_client)
    
    def desable_delete_bt(self):
        self.delete_window.confirm_bt.configure(state="disabled")

    def clean_cpf_entry(self):
        self.delete_window.primary_key_entry.delete(0, "end")

    def close_alert_window(self):
        self.alert_window.withdraw()

    def deleting_client(self):
        try:
            message = self.delete_controller.deleting_client(self.cpf)
            self.delete_window.tb.configure(state="normal", text_color='green')
            self.delete_window.tb.delete("1.0", "end")
            self.delete_window.tb.insert(index='0.0', text=message)
            self.delete_window.tb.configure(state="disabled")
        except Exception as err:
            self.delete_window.tb.configure(state="normal", text_color="red")
            self.delete_window.tb.delete("1.0", "end")
            self.delete_window.tb.insert(index='0.0', text=err)
            self.delete_window.tb.configure(state="disabled")

    def alertWindowCall(self):
        self.alert_window = AlertWindow()
        self.alert_window.yes_bt.configure(command=lambda: [self.deleting_client(), self.close_alert_window(), self.clean_cpf_entry(), self.desable_delete_bt()])

    def delete_button_command(self):
        self.delete_window.confirm_bt.configure(state='normal')
        self.delete_window.confirm_bt.configure(command=self.alertWindowCall)

        



        
            

    
      
    

