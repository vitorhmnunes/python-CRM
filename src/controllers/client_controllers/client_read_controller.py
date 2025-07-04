from src.models.crud_operations import DbCRUDOperations
from src.models.validators.validators import ClientValidators, isNull

class ClientReadController():
    def __init__(self):
        self.db_operations = DbCRUDOperations()
        self.validator = ClientValidators()

    def read_db_record(self, cpf_value):
        try:
            message = self.db_operations.read_record(table_name='client', condition_column='cpf', condition_value=cpf_value)
            return message
        except Exception as err:
            raise err
            

    def validating(self, cpf_value):
        try :
            isNull([cpf_value])
            self.validator.cpf_validations(cpf_value)
        except ValueError as err:
            raise err
        
    def exists_cpf(self, table_name, cpf_value):
        verification = self.db_operations.verify_condition(table_name, condition_column='cpf', condition_value=cpf_value)
        if verification == False:
            raise Exception(f"Cpf = {cpf_value} doesn't exists")
       

    def reading_client(self, cpf_value):
        try:
            self.validating(cpf_value)
            self.exists_cpf(table_name='client', cpf_value=cpf_value)
        except Exception as err:
            raise err
        else:
            try: 
                message = self.read_db_record(cpf_value)
                return message
            except Exception as err:
                raise err
    