from src.models.entities.client import Client
from src.models.crud_operations import DbCRUDOperations
from src.models.validators.validators import ClientValidators, isNull

class ClientUpdateController():
    def __init__(self):
        self.db_operations = DbCRUDOperations()
        self.validator = ClientValidators()

    def update_db_record(self, client: Client):
        client_dict = {
            'name': client.name,
            'adress': client.adress,
            'phone_number': client.phone_number
        }

        try:
            message = self.db_operations.update_record_by_id(table_name='client', condition_column='cpf', condition_value=client.cpf, update_data=client_dict)
            return message
        except Exception as err:
            raise err
            

    def validating(self, client: Client):
        try :
            isNull([client.cpf, client.name, client.adress, client.phone_number])
            self.validator.cpf_validations(client.cpf)
            self.validator.name_validations(client.name)
            self.validator.phone_number_validations(client.phone_number)
        except ValueError as err:
            raise err
        
    def exists_cpf(self, table_name, cpf_value):
        verification = self.db_operations.verify_condition(table_name, condition_column='cpf', condition_value=cpf_value)
        if verification == False:
            raise Exception(f"Cpf = {cpf_value} doesn't exists")
       

    def updating_client(self, data: dict):
        client = Client(data['cpf'], data['name'], data['adress'], data['phone_number'])
        try:
            self.validating(client)
            self.exists_cpf(table_name='client', cpf_value=client.cpf)
        except Exception as err:
            raise err
        else:
            try: 
                message = self.update_db_record(client)
                return message
            except Exception as err:
                raise err