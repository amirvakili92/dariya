import pandas as pd
import 


# Class for reading the data and cleaning NaN rows and columns
class DataLoader:
    def __init__(self, file_path=None):
        self.df = None
        if file_path:
            self.read_file(file_path)

    def read_file(self, file_path):
        """
        Read CSV file and remove rows and columns with all NaN values.
        """
        self.df = pd.read_csv(file_path, low_memory=False)
        # Drop rows where all values are NaN
        self.df = self.df.dropna(how='all')
        # Drop columns where all values are NaN
        self.df = self.df.dropna(axis=1, how='all')
        return self.df

    def get_data(self):
        """
        Return the loaded dataframe.
        """
        return self.df


