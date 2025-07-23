from src.views.rent_window.rent_update_window import RentUpdateWindow, UpdateInfosToplevelWindow
from src.controllers.rent_controllers.rent_read_controller import RentReadController
from src.controllers.rent_controllers.rent_update_controller import RentUpdateController

class RentUpdateWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.update_window = RentUpdateWindow(self.right_frame)
        self.read_controller = RentReadController()
        self.update_controller = RentUpdateController()
        self.read_button_command()

    def get_rent_code(self):
        code = self.update_window.primary_key_entry.get()
        return code

    def formating_db_return(self, dict_list):
        values_list = list(dict_list[0].values())
        message = f"Code: {values_list[0]} || CPF: {values_list[1]} || Vehicle Code: {values_list[2]}\n Inicial Date: {values_list[3]} || Final Date: {values_list[4]}"
        return message

    def reading_rent(self):
        self.code = self.get_rent_code()
        try:
            message = self.read_controller.reading_rent(self.code)
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
        self.update_window.send_bt.configure(command=self.reading_rent)

    def desable_update_bt(self):
        self.update_window.confirm_bt.configure(state="disabled")

    def clean_code_entry(self):
        self.update_window.primary_key_entry.delete(0, "end")

    def close_toplevel_window(self):
        self.toplevel_window.withdraw()

    def get_rent_data(self) -> dict:
        cpf = self.code
        vehicle_code = self.toplevel_window.vehicle_code_entry.get()
        inicial_date = self.toplevel_window.inicial_date_entry.get()
        final_date = self.toplevel_window.final_date_entry.get()
        
        data_dict = {
            'cpf': cpf,
            'vehicle_code': vehicle_code,
            'inicial_date': inicial_date,
            'final_date': final_date
        }

        return data_dict

    def updating_rent(self):
        rent_data = self.get_rent_data()
        try:
            message = self.update_controller.updating_rent(self.code, rent_data)
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
        self.toplevel_window.update_submit_button.configure(command=lambda: [self.updating_rent(), self.desable_update_bt(), self.clean_code_entry()])

    def update_button_command(self):
        self.update_window.confirm_bt.configure(state='normal')
        self.update_window.confirm_bt.configure(command=self.infos_window_call)