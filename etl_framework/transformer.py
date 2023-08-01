import configparser
import pandas as pd
import sqlite3
from sqlite3 import Error

class Transformer:

    def __init__(self, extracted_file):
        self.extracted_file = extracted_file
        print("Transformer initialised.")

    def clear_row_if_empty_column(self, extracted_file):
        print("Removing rows with an empty column...")
        extracted_file = extracted_file.dropna(axis = 0, how = 'any', inplace = False, ignore_index = False)
        print("Removed.")
        return extracted_file

    def clear_duplicate_values(self, extracted_file):
        print("Removing duplicate rows...")
        extracted_file = extracted_file.drop_duplicates(subset = None, keep = 'first', inplace = False, ignore_index = False)
        print("Removed.")
        return extracted_file