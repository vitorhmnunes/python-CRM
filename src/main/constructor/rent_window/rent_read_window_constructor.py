from src.views.rent_window.rent_read_window import RentReadWindow
from src.controllers.rent_controllers.rent_read_controller import RentReadController

class RentReadWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.read_window = RentReadWindow(self.right_frame)
        self.controller = RentReadController()
        self.button_command()

    def get_rent_code(self):
        code = self.read_window.primary_key_entry.get()
        return code

    def formating_db_return(self, dict_list):
        values_list = list(dict_list[0].values())
        message = f"Code: {values_list[0]} || CPF: {values_list[1]} || Vehicle Code: {values_list[2]}\n Inicial Date: {values_list[3]} || Final Date: {values_list[4]}"
        return message

    def reading_rent(self):
        code = self.get_rent_code()
        try:
            message = self.controller.reading_rent(code)
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
        self.read_window.send_bt.configure(command=self.reading_rent)