from datetime import date

class Rent:
    def __init__(self, cpf:str, vehicle_id:int, inicial_date:date, final_date:date):
        self.cpf = cpf 
        self.vehicle_id = vehicle_id
        self.inicial_date = inicial_date
        self.final_date = final_date

