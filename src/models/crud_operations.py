from src.models.database_connection import MySQLConnection

class DbCRUDOperations:
    def __init__(self):
        self.connection = MySQLConnection()
        self.conn = self.connection.conn

    def _querying(self, query: str):
        if (not self.conn.is_connected()) or self.connection is None:
            self.conn = self.connection.conn
        
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result
    
    def closing(self):
        if self.conn.is_connected():
            self.conn.close()
    
    def _get_list_of_database_tables(self):
        list_of_tables = self._querying('SHOW tables;')
        tables = []
        for item in list_of_tables:
            for table in item.values():
                tables.append(table)        

        return tables
    
    def _is_on_Database(self, table_name: str) -> None:
        if table_name not in self._get_list_of_database_tables():
            raise Exception(f'Table not found in {self.connection.get_database()} database')
        
        
    def _execute_query_with_dict(self, query: str, attr: dict):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query, params=attr) #%(key)s
        except TypeError as err:
            raise (f'An error occur during the insert '
                   f'operation on {self.connection.get_database()}\n Message3:'
                   f'{err}')

    def _returning_key_list_and_placeholders(self, attr: dict):
        keys_list = ', '.join([key for key in attr.keys()])
        placeholder = ', '.join([f'%({key})s' for key in attr.keys()])

        return keys_list, placeholder

    
    def get_lines_from_tables(self, table: str, attribute, search_key):
        query = ' '.join(['SELECT * FROM', table, 'WHERE', attribute, '=', search_key, ';'])
        result = self._querying(query)

        return result

    def create_line(self, table_name: str ,attr: dict):
        self._is_on_Database(table_name)
        key_list, placeholders = self._returning_key_list_and_placeholders(attr)
        insertion_query = f"INSERT INTO {table_name} ({key_list}) VALUES ({placeholders})"
        try:
            self._execute_query_with_dict(insertion_query, attr)
        except Exception as err:
            raise f'Massage: {err}'
        
        self.conn.commit()
        return f"Instance_created on {table_name}"

    def read_line(self, table_name, attr, attr_value):
        self._is_on_Database(table_name)
        return self.get_lines_from_tables(table=table_name, attribute=attr, search_key=attr_value)
    

    # def update_instance_by_id(self, table_name: str, attr: dict):
    #     self._is_on_Database(table_name)
    #     key_list, placeholders = self._returning_key_list_and_placeholders(attr)
    #     update_query = f"UPDATE {table_name} MODIFY ({key_list})"

    #     self.conn.commit()


    def delete_instance(self, table_name: str, condition: str, value):
        self._is_on_Database(table_name)
        delete_query = f"DELETE FROM {table_name} WHERE {condition} = %s"
        self._execute_query_with_dict(delete_query, value)

        self.conn.commit()
        return f"Instance deleted on {table_name}"
