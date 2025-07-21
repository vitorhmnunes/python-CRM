from src.models.entities.vehicle import Vehicle
from src.models.crud_operations import DbCRUDOperations
from src.models.validators.validators import VehicleValidators, isNull

class VehicleUpdateController():
    def __init__(self):
        self.db_operations = DbCRUDOperations()
        self.validator = VehicleValidators()

    def update_db_record(self, vehicle: Vehicle):
        vehicle_dict = {
            'category': vehicle.category,
            'fuel': vehicle.fuel,
            'year': vehicle.year,
            'model': vehicle.model
        }

        try:
            message = self.db_operations.update_record(table_name='vehicle', condition_column='code', condition_value=vehicle.code, update_data=vehicle_dict)
            return message
        except Exception as err:
            raise err         

    def validating(self, vehicle: Vehicle):
        try :
            isNull([vehicle.category, vehicle.fuel, vehicle.year, vehicle.model])
            self.validator.year_validation(vehicle.year)
        except ValueError as err:
            raise err
        
    def exists_code(self, table_name, code_value):
        verification = self.db_operations.verify_condition(table_name, condition_column='code', condition_value=code_value)
        if verification == False:
            raise Exception(f"Code = {code_value} doesn't exist")


    def updating_vehicle(self, data: dict):
        vehicle = Vehicle(data['code'], data['category'], data['fuel'], data['year'], data['model'])
        try:
            self.validating(vehicle)
            self.exists_code(table_name='vehicle', code_value=vehicle.code)
        except Exception as err:
            raise err
        else:
            try: 
                message = self.update_db_record(vehicle)
                return message
            except Exception as err:
                raise err