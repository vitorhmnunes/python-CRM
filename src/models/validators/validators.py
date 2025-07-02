import re
from datetime import datetime, date

def isNull(attribute_list):
    for attr in attribute_list:
        if not str(attr):
            raise ValueError('All fields must be filled in')

class ClientValidators():
    def cpf_validations(self, cpf):
        cpf_copy = cpf
        cpf_copy = re.sub('[.-]', '', cpf_copy )

        if len(cpf) != 14:
            raise ValueError ("Cpf error. Expected format (000.000.000-00)")
        elif (cpf[3] != '.') or (cpf[7] != '.') or (cpf[11] != '-'):
            raise ValueError ("Cpf error. Expected format (000.000.000-00)")
        elif not cpf_copy.isnumeric():
            raise ValueError("Cpf error. Must be numeric.")

    def name_validations(self, name: str):
        for letter in name:
            if letter.isdigit():
                raise ValueError("Name error. Can't be numeric")

    def phone_number_validations(self, phone_number):
        phone_copy = phone_number
        phone_copy = re.sub('[()-]', '', phone_copy) 

        if len(phone_number) != 14:
            raise ValueError("Phone_number error. Expected format ((00)00000-0000)")
        elif (phone_number[0] != '(') or (phone_number[3] != ')') or (phone_number[9] != '-'):
            raise ValueError("Phone_number error. Expected format ((00)00000-0000)")
        elif not phone_copy.isnumeric():
            raise ValueError("Phone_number error. Must be numeric.")


class VehicleValidators():
    def code_validation(self, code):
        try: 
            int(code)
        except: 
            raise ValueError("Code error. Must be numeric")

    def year_validation(self, year: str):
        if len(year) != 4:
            raise ValueError ("Year error. Expected format (0000)")
        elif not year.isnumeric():
            raise ValueError("Year error. Must be numeric")
        elif year > (date.today().year + 1):
            raise ValueError(f"Year error. Must be lower than {(date.today().year + 1)}")



class RentValidators():   
    def inicial_date_validation(self, inicial_date: str, final_date: str):
        format = "%d/%m/%Y"
        try: 
            inicial_date = datetime.strptime(inicial_date, format).date()
            final_date = datetime.strptime(final_date, format).date()
        except ValueError:
            raise "Date error. Invalid format, expected (00/00/0000)."

        if inicial_date > final_date:
            raise ValueError("Date error. Inicial date greater than final date.")
        elif inicial_date == final_date:
            raise ValueError("Date error. Inicial date equal to final date.")

        
        