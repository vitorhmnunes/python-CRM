from src.views.vehicle_window.vehicle_delete_window import VehicleDeleteWindow
from src.views.base_structures.alert_window import AlertWindow
from src.controllers.vehicle_controllers.vehicle_delete_controller import VehicleDeleteController
from src.controllers.vehicle_controllers.vehicle_read_controller import VehicleReadController

class VehicleDeleteWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.delete_window = VehicleDeleteWindow(self.master)
        self.read_controller = VehicleReadController()
        self.delete_controller = VehicleDeleteController()
        self.read_button_command()

    def get_vehicle_code(self):
        code = self.delete_window.primary_key_entry.get()
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
        self.delete_window.send_bt.configure(command=self.reading_vehicle)
    
    def desable_delete_bt(self):
        self.delete_window.confirm_bt.configure(state="disabled")

    def clean_code_entry(self):
        self.delete_window.primary_key_entry.delete(0, "end")

    def close_alert_window(self):
        self.alert_window.withdraw()

    def deleting_vehicle(self):
        try:
            message = self.delete_controller.deleting_vehicle(self.code)
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
        self.alert_window.yes_bt.configure(command=lambda: [self.deleting_vehicle(), self.close_alert_window(), self.clean_code_entry(), self.desable_delete_bt()])

    def delete_button_command(self):
        self.delete_window.confirm_bt.configure(state='normal')
        self.delete_window.confirm_bt.configure(command=self.alertWindowCall)

        
