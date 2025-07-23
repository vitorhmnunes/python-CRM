from src.views.vehicle_window.vehicle_read_window import VehicleReadWindow
from src.controllers.vehicle_controllers.vehicle_read_controller import VehicleReadController

class VehicleReadWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.read_window = VehicleReadWindow(self.master)
        self.controller = VehicleReadController()
        self.button_command()

    def get_vehicle_code(self):
        code = self.read_window.primary_key_entry.get()
        return code

    def formating_db_return(self, dict_list):
        values_list = list(dict_list[0].values())
        message = f"Code: {values_list[0]} || Model: {values_list[4]} || Fuel: {values_list[2]}\n Year: {values_list[3]} || Category: {values_list[1]}"
        return message

    def reading_vehicle(self):
        print('starting')
        cpf = self.get_vehicle_code()
        try:
            message = self.controller.reading_vehicle(cpf)
            values_string = self.formating_db_return(message)
            print('sending data to controller')
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
        self.read_window.send_bt.configure(command=self.reading_vehicle)