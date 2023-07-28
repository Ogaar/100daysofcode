import configparser
import pandas as pd
import sqlite3
from sqlite3 import Error

class Loader:

    def __init__(self, load_format):
        if load_format.lower() not in ["csv", "excel", "sqlite"]:
            raise Exception("That is not a valid load format.")
        self.load_format = load_format.lower()
        print("Loader initialised.")

    def load(self, df):
        print("Loading...")
        config = configparser.ConfigParser()
        config.read('C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\etl_framework\\configs'
                    '\\loader_configs.ini')

        if self.load_format == "csv":
            self.__csv_load(config, df)
        elif self.load_format == "sqlite":
            self.__sqlite_load(config,df)
        elif self.load_format == "excel":
            self.__excel_load(config, df)


    def __csv_load(self, config, df):
        csv_file = config.get('CSV', 'file_new_location')
        try:
            df = df.to_csv(csv_file, index=False)
            return df
        except Exception as e:
            print("Error while reading file: check configs")
            print("Exception: " + str(e))

    def __excel_load(self, config, df):
        excel_file = config.get('EXCEL', 'file_new_location')
        try:
            df = df.to_excel(excel_file, index=False)
            return df
        except Exception as e:
            print("Error while reading file: check configs")
            print("Exception: " + str(e))

    def __sqlite_load(self, config, df):
        sqlite_file = config.get('SQLITE', 'database_location')
        table_name = config.get('SQLITE', 'table_name')
        if_exists = config.get('SQLITE', 'if_exists')
        conn = self.__create_sql_connection(sqlite_file)
        print("Database connection created.")
        df_columns = df.columns
        df_dtypes = df.dtypes
        print("Creating database query...")
        query = f'Create table if not Exists {table_name} ('
        for i in range(0, len(df_columns)):
            dtype = str(df_dtypes[i])
            if "float64" in dtype:
                dtype = "real"
            if "object" in dtype:
                dtype = "text"
            if "int64" in dtype:
                dtype = "integer"
            query += df_columns[i] + " " + dtype + ","
        query = query[:-1]
        query += ")"
        print("Database query created.\nQuery: " + query)
        print("Executing...")
        conn.execute(query)
        df.to_sql(table_name, conn, if_exists = if_exists, index=False)
        conn.commit()
        print("Executed.")
        print("Closing connection...")
        conn.close()


    def __create_sql_connection(self, db_file):
        print("Creating database connection...")
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
