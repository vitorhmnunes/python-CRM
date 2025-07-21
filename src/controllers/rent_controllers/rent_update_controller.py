from src.models.entities.rent import Rent
from src.models.crud_operations import DbCRUDOperations
from src.models.validators.validators import RentValidators, VehicleValidators, isNull
from datetime import datetime


class RentUpdateController():
    def __init__(self):
        self.db_operations = DbCRUDOperations()
        self.validator = RentValidators()
        self.vehicle_code_validator = VehicleValidators()

    def update_db_record(self, rent_code, rent: Rent):
        rent_dict = {
            'vehicle_code': rent.vehicle_code,
            'inicial_date': rent.inicial_date,
            'final_date': rent.final_date
        }

        try:
            message = self.db_operations.update_record(table_name='rent', condition_column='code', condition_value=rent_code, update_data= rent_dict)
            return message
        except Exception as err:
            raise err
            
    def validating(self, rent_code, rent: Rent):
        try :
            isNull([rent_code, rent.cpf, rent.vehicle_code, rent.inicial_date, rent.final_date])
            self.validator.rent_code_validation(rent_code)
            self.validator.exists_rent_code(rent_code)
            self.vehicle_code_validator.code_validation(rent.vehicle_code)
            self.validator.exists_vehicle_code(rent.vehicle_code)
            self.validator.date_syntax_validation(rent.inicial_date, rent.final_date)
        except ValueError as err:
            raise err
    
    def data_to_datetime(self, rent: Rent):
        format = "%d/%m/%Y"
        rent.inicial_date = datetime.strptime(rent.inicial_date, format).date()
        rent.final_date = datetime.strptime(rent.final_date, format).date()
    
    def dates_and_rental_period_validation(self, rent: Rent):
        self.data_to_datetime(rent)
        try:
            self.validator.inicial_date_validation(rent.vehicle_code, rent.inicial_date)
            self.validator.final_date_validation(rent.vehicle_code, rent.final_date)
            self.validator.rental_period_validation(rent.vehicle_code, rent.inicial_date, rent.final_date)
        except Exception as err:
            raise err


    def updating_rent(self,rent_code, data: dict):
        rent = Rent(data['cpf'], data['vehicle_code'], data['inicial_date'], data['final_date'])
        try:
            self.validating(rent_code, rent)
            self.dates_and_rental_period_validation(rent)
        except Exception as err:
            raise err
        else:   
            try: 
                message = self.update_db_record(rent_code, rent)
                return message
            except Exception as err:
                raise err