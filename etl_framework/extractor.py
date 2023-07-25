import configparser
import pandas as pd
class Extractor:
    def __init__(self, extract_format):
        self.extract_format = extract_format
        print("Extractor initialised.")

    def extract(self):
        print("Extracting...")
        # csv, sql, excel, html
        config = configparser.ConfigParser()
        config.read('C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\etl_framework\\configs'
                    '\\extractor_configs.ini')
        if self.extract_format == "csv":
            extracted_file = self.__csv_extract(config)
        # elif extract_format == "sql":
        #
        # elif extract_format == "excel":
        #
        # elif extract_format == "html":

        return extracted_file

    def __csv_extract(self, config):
        csv_file = config.get('CSV', 'file_name_location')
        try:
            df = pd.read_csv(csv_file)
            return df
        except Exception as e:
            print("Error while reading file: check configs")
            print("Exception: " + str(e))
