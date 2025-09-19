import pandas as pd
import numpy as np


# read csv and xlsx
class DataLoad:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        if 'csv' in self.file_path:
            data = pd.read_csv(self.file_path)
            data = data.dropna(how='all')
            return data
        if 'xlsx'in self.file_path:
            return pd.read_excel(self.file_path)
        else:
            return ''

