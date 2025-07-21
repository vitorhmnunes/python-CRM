from src.models.crud_operations import DbCRUDOperations
from src.models.validators.validators import RentValidators, isNull

class RentReadController():
    def __init__(self):
        self.db_operations = DbCRUDOperations()
        self.validator = RentValidators()

    def read_db_record(self, rent_code):
        try:
            message = self.db_operations.read_record(table_name='rent', condition_column='code', condition_value=rent_code)
            return message
        except Exception as err:
            raise err
            
    def validating(self, rent_code):
        try :
            isNull([rent_code])
            self.validator.rent_code_validation(rent_code)
            self.validator.exists_rent_code(rent_code)
        except ValueError as err:
            raise err

    def reading_rent(self, rent_code):
        try:
            self.validating(rent_code)
        except Exception as err:
            raise err
        else:   
            try: 
                message = self.read_db_record(rent_code)
                return message
            except Exception as err:
                raise err