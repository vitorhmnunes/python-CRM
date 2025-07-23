from src.views.start_window import StartWindow
from src.main.constructor.base_structures.upper_menu_buttons_constructor import UpperMenuButtonsConstructor
from src.controllers.client_controllers.client_read_controller import ClientReadController
from src.controllers.rent_controllers.rent_read_controller import RentReadController
from src.models.crud_operations import DbCRUDOperations
from src.models.validators.validators import VehicleValidators, RentValidators, isNull

class StartWindowConstructor():
    def __init__(self, root):
        self.root = root
        self.start_window = StartWindow(self.root)
        self.upper_buttons = UpperMenuButtonsConstructor(
                                                          self.start_window.upper_frame, 
                                                          self.root, self.start_window.frame
                                                          )
        self.client_controller = ClientReadController()
        self.rent_controller = RentReadController()
        self.cpf_button_command()
        self.rent_code_button_command()
        self.vehicle_code_button_command()

    def get_cpf(self):
        cpf = self.start_window.cpf_entry.get()
        return cpf

    def formating_client_data(self, dict_list):
        values_list = list(dict_list[0].values())
        message = f"CPF: {values_list[0]} || Name: {values_list[1]}\nAdress: {values_list[2]} || Phone Number: {values_list[3]}\n"
        return message

    def reading_client(self):
        cpf = self.get_cpf()
        try:
            message = self.client_controller.reading_client(cpf)
            values_string = self.formating_client_data(message)
            self.start_window.client_tb.configure(state="normal", text_color='white')
            self.start_window.client_tb.delete("1.0", "end")
            self.start_window.client_tb.insert(index='0.0', text=values_string)
            self.start_window.client_tb.configure(state="disabled")
        except Exception as err:
            self.start_window.client_tb.configure(state="normal", text_color="red")
            self.start_window.client_tb.delete("1.0", "end")
            self.start_window.client_tb.insert(index='0.0', text=err)
            self.start_window.client_tb.configure(state="disabled")

    def cpf_button_command(self):
        self.start_window.cpf_search_button.configure(command=self.reading_client)

    def get_rent_code(self):
        code = self.start_window.rent_code_entry.get()
        return code

    def formating_rent_data(self, dict_list):
        rents_string = ''
        for i in dict_list:
            rent = f"Code: {i['code']} || CPF: {i['cpf']} || Vehicle Code: {i['vehicle_code']}\n Inicial Date: {i['inicial_date']} || Final Date: {i['final_date']}\n\n"
            rents_string = rents_string + rent
        return rents_string

    def reading_rent_by_rent_code(self):
        rent_code = self.get_rent_code()
        try:
            rents_dict = self.rent_controller.reading_rent(rent_code)
            rents_string = self.formating_rent_data(rents_dict)
            self.start_window.rent_tb.configure(state="normal", text_color='white')
            self.start_window.rent_tb.delete("1.0", "end")
            self.start_window.rent_tb.insert(index='0.0', text=rents_string)
            self.start_window.rent_tb.configure(state="disabled")
        except Exception as err:
            self.start_window.rent_tb.configure(state="normal", text_color="red")
            self.start_window.rent_tb.delete("1.0", "end")
            self.start_window.rent_tb.insert(index='0.0', text=err)
            self.start_window.rent_tb.configure(state="disabled")

    def rent_code_button_command(self):
        self.start_window.rent_code_button.configure(command=self.reading_rent_by_rent_code)

    def get_vehicle_code(self):
        vcode = self.start_window.vehicle_code_entry.get()
        return vcode
    
    def querying_rent_by_vehicle_code(self, vehicle_code):
        dboperation = DbCRUDOperations()
        query = f'SELECT * FROM rent WHERE vehicle_code = "{vehicle_code}";'
        message = dboperation.querying(query)
        if not message:
            raise Exception(f"No rents with vehicle code = {vehicle_code}")
        else:
            return message
        
    def validating_vehicle_code(self, vehicle_code):
        self.vehicle_validator = VehicleValidators()
        self.rent_validator = RentValidators()
        try:
            isNull([vehicle_code])
            self.vehicle_validator.code_validation(vehicle_code)
            self.rent_validator.exists_vehicle_code(vehicle_code)
        except Exception as err:
            raise err

    def reading_rent_by_vehicle_code(self):
        vcode = self.get_vehicle_code()
        try:
            self.validating_vehicle_code(vcode)
            rents_dict = self.querying_rent_by_vehicle_code(vcode)
            rents_string = self.formating_rent_data(rents_dict)
            self.start_window.rent_tb.configure(state="normal", text_color='white')
            self.start_window.rent_tb.delete("1.0", "end")
            self.start_window.rent_tb.insert(index='0.0', text=rents_string)
            self.start_window.rent_tb.configure(state="disabled")
        except Exception as err:
            self.start_window.rent_tb.configure(state="normal", text_color="red")
            self.start_window.rent_tb.delete("1.0", "end")
            self.start_window.rent_tb.insert(index='0.0', text=err)
            self.start_window.rent_tb.configure(state="disabled")


    def vehicle_code_button_command(self):
        self.start_window.vehicle_code_button.configure(command=self.reading_rent_by_vehicle_code)






