import mysql.connector as mysql_connector
from src.models.database_connection import MySQLConnection

class DbCRUDOperations:
    def __init__(self):
        self.connection = MySQLConnection()
        self.conn = self.connection.get_db_connection()

    def _querying(self, query: str):
        if (not self.conn.is_connected()) or self.connection is None:
            self.conn = self.connection.get_db_connection()
        
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result
    
    def closing(self):
        if self.conn.is_connected():
            self.conn.close()
    
    '''
    ----- Functions for verifying if the table exists
    def _get_list_of_database_tables(self):
        list_of_tables = self._querying('SHOW tables;')
        tables = []
        for item in list_of_tables:
            for table in item.values():
                tables.append(table)        

        return tables
    
    def _verify_table(self, table_name: str) -> None:
        if table_name not in self._get_list_of_database_tables():
            raise Exception(f'Table not found in {self.connection.get_database()} database')'''
        

    def _returning_columns_and_values(self, data: dict):
        columns = []
        values = []
        for column, value in data.items():
            columns.append(column)
            values.append(value)

        return columns, values

    def _get_line_from_table(self, table_name: str, condition_column: str, condition_value):
        query = ' '.join(['SELECT * FROM', table_name, 'WHERE', condition_column, '=', condition_value, ';'])
        result = self._querying(query)
        return result
  
        
    def _verify_condition(self, table_name: str, condition_column: str, condition_value):
        result = self._get_line_from_table(table_name, condition_column, condition_value)
        if not result:
            raise Exception(f"{condition_value} not found")



    def read_record(self, table_name: str, condition_column: str, condition_value):
        result = self._get_lines_from_tables(table_name, condition_column, condition_value)
        return result
        

    def create_record(self, table_name: str, data: dict):
        columns, values = self._returning_columns_and_values(data)

        # Construct the VALUES part of the query
        value_syntax = []
        for value in values:
            value_syntax.append("%s")

        insertion_query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({','.join(value_syntax)});"

        try:
            cursor = self.conn.cursor()
            cursor.execute(insertion_query, tuple(data))
            self.conn.commit()
            message = (f"Row created in {table_name}")
            return message
        
        except mysql_connector.Error as err:
            self.conn.rollback()
            message = (f"Error creating instance: {err}")
            raise message


    def update_record_by_id(self, table_name: str, condition_column: str, condition_value, update_data: dict):
        columns, values = self._returning_columns_and_values(update_data)

        # Construct the SET part of the query (column = %s)
        column_list = []
        for column in columns:
            column_list.append(f"{column} = %s")

        update_query = f"UPDATE {table_name} SET {','.join(column_list)} WHERE {condition_column} = %s;"

        values.append(condition_value)   

        try:
            cursor = self.conn.cursor()
            cursor.execute(update_query, tuple(values))
            self.conn.commit()
            message = (f"Row ({condition_column} = {condition_value}) updated in {table_name}")
            return message
        
        except mysql_connector.Error as err:
            self.conn.rollback()
            message = (f'Error updating data: {err}')
            return message


    def delete_record(self, table_name: str, condition_column: str, condition_value):
        delete_query = f"DELETE FROM {table_name} WHERE {condition_column} = %s"

        try:
            cursor = self.conn.cursor()
            cursor.execute(delete_query, [condition_value])
            self.conn.commit()
            message = (f"Row ({condition_column} = {condition_value}) deleted in {table_name}")
            return message
        
        except mysql_connector.Error as err:
            self.conn.rollback()
            message = (f'Error deleting data: {err}')
            return message  
