from src.views.vehicle_window.vehicle_update_window import VehicleUpdateWindow, UpdateInfosToplevelWindow
from src.controllers.vehicle_controllers.vehicle_update_controller import VehicleUpdateController
from src.controllers.vehicle_controllers.vehicle_read_controller import VehicleReadController

class VehicleUpdateWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.update_window = VehicleUpdateWindow(self.master)
        self.read_controller = VehicleReadController()
        self.update_controller = VehicleUpdateController()
        self.read_button_command()

    def get_vehicle_code(self):
        code = self.update_window.primary_key_entry.get()
        return code

    def formating_db_return(self, dict_list):
        values_list = list(dict_list[0].values())
        message = f"Code: {values_list[0]} || Model: {values_list[4]} || Fuel: {values_list[2]}\n Year: {values_list[3]} || Category: {values_list[1]}"
        return message

    def reading_vehicle(self):
        self.code = self.get_vehicle_code()
        try:
            message = self.read_controller.reading_vehicle(self.code)
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
        self.update_window.send_bt.configure(command=self.reading_vehicle)

    def desable_update_bt(self):
        self.update_window.confirm_bt.configure(state="disabled")

    def clean_code_entry(self):
        self.update_window.primary_key_entry.delete(0, "end")

    def close_toplevel_window(self):
        self.toplevel_window.withdraw()

    def get_vehicle_data(self) -> dict:
        code = self.code
        category = self.toplevel_window.cat_entry.get()
        fuel = self.toplevel_window.fuel_entry.get()
        year = self.toplevel_window.year_entry.get()
        model = self.toplevel_window.model_entry.get()
        
        data_dict = {
            'code': code,
            'category': category,
            'fuel': fuel,
            'year': year,
            'model': model
        }

        return data_dict

    def updating_vehicle(self):
        vehicle_data = self.get_vehicle_data()
        try:
            message = self.update_controller.updating_vehicle(vehicle_data)
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
        self.toplevel_window.vehicle_submit_button.configure(command=lambda: [self.updating_vehicle(), self.desable_update_bt(), self.clean_code_entry()])

    def update_button_command(self):
        self.update_window.confirm_bt.configure(state='normal')
        self.update_window.confirm_bt.configure(command=self.infos_window_call)