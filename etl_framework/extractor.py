import configparser
import pandas as pd
import sqlite3
from sqlite3 import Error

class Extractor:
    def __init__(self, extract_format):
        if extract_format.lower() not in ["csv", "excel", "sqlite"]:
            raise Exception("That is not a valid extract format.")
        self.extract_format = extract_format.lower()
        print("Extractor initialised.")

    def extract(self):
        print("Extracting...")
        # csv, sql, excel, html
        config = configparser.ConfigParser()
        config.read('C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\etl_framework\\configs'
                    '\\extractor_configs.ini')
        if self.extract_format == "csv":
            extracted_file = self.__csv_extract(config)
        elif self.extract_format == "sqlite":
            extracted_file = self.__sqlite_extract(config)
        elif self.extract_format == "excel":
            extracted_file = self.__excel_extract(config)

        return extracted_file

    def __csv_extract(self, config):
        csv_file = config.get('CSV', 'file_name_location')
        try:
            df = pd.read_csv(csv_file)
            return df
        except Exception as e:
            print("Error while reading file: check configs")
            print("Exception: " + str(e))

    def __sqlite_extract(self, config):
        sqlite_file = config.get('SQLITE', 'database_location')
        table_name = config.get('SQLITE', 'table_name')
        conn = self.__create_sql_connection(sqlite_file)
        print("Database connection created.")
        df = pd.read_sql_query("SELECT * FROM " + table_name, conn)
        conn.commit()
        print("Closing connection...")
        conn.close()
        return df


    def __create_sql_connection(self, db_file):
        print("Creating database connection...")
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

    def __excel_extract(self, config):
        excel_file = config.get('EXCEL', 'file_name_location')
        try:
            df = pd.read_excel(excel_file)
            return df
        except Exception as e:
            print("Error while reading file: check configs")
            print("Exception: " + str(e))

