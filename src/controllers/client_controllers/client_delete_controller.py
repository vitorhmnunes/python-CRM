from src.models.crud_operations import DbCRUDOperations
from src.models.validators.validators import ClientValidators, isNull

class ClientDeleteController():
    def __init__(self):
        self.db_operations = DbCRUDOperations()
        self.validator = ClientValidators()

    def delete_db_record(self, cpf_value):
        try:
            message = self.db_operations.delete_record(table_name='client', condition_column='cpf', condition_value=cpf_value)
            return message
        except Exception as err:
            raise err
            

    def validating(self, cpf_value):
        try :
            isNull([cpf_value])
            self.validator.cpf_validations(cpf_value)
        except ValueError as err:
            raise err
       

    def deleting_client(self, cpf_value):
        try:
            self.validating(cpf_value)
        except Exception as err:
            raise err
        else:
            try: 
                message = self.delete_db_record(cpf_value)
                return message
            except Exception as err:
                raise err