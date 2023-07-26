import configparser
import pandas as pd

class Loader:

    def __init__(self, load_format):
        if load_format.lower() not in ["csv", "excel", "sql"]:
            raise Exception("That is not a valid load format.")
        self.load_format = load_format.lower()
        print("Loader initialised.")

    def load(self, df):
        print("Loading...")
        config = configparser.ConfigParser()
        config.read('C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\etl_framework\\configs'
                    '\\loader_configs.ini')

        if self.load_format == "csv":
            loaded_file = self.__csv_load(config, df)
        # elif extract_format == "sql":
        #
        elif self.load_format == "excel":
            loaded_file = self.__excel_load(config, df)


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