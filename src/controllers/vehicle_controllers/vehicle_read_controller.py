from src.models.crud_operations import DbCRUDOperations
from src.models.validators.validators import VehicleValidators, isNull

class VehicleReadController():
    def __init__(self):
        self.db_operations = DbCRUDOperations()
        self.validator = VehicleValidators()

    def read_db_record(self, code_value):
        try:
            message = self.db_operations.read_record(table_name='vehicle', condition_column='code', condition_value=code_value)
            return message
        except Exception as err:
            raise err

    def validating(self, code_value):
        try :
            isNull([code_value])
            self.validator.code_validation(code_value)
        except ValueError as err:
            raise err
    
    def exists_code(self, table_name, code_value):
        verification = self.db_operations.verify_condition(table_name, condition_column='code', condition_value=code_value)
        if verification == False:
            raise Exception(f"Code = {code_value} doesn't exist")
       
    def reading_vehicle(self, code_value):
        try:
            self.validating(code_value)
            self.exists_code(table_name='vehicle', code_value=code_value)
        except Exception as err:
            raise err
        else:
            try: 
                message = self.read_db_record(code_value)
                return message
            except Exception as err:
                raise err