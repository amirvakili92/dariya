import pandas as pd
import numpy as np
import re

class DataCleaner:
    def __init__(self, dataframe):
        self.df = dataframe

    def clean_number(self, price_str):
        """
        Clean price string by removing non-numeric characters and convert to float.
        """
        price_str = str(price_str)
        
        # Remove all non-numeric characters except period
        cleaned_str = re.sub(r'[^0-9.]', '', price_str)
        
        # If there are multiple dots, keep only the first one
        if cleaned_str.count('.') > 1:
            cleaned_str = cleaned_str.split('.')[0] + '.' + cleaned_str.split('.')[1].replace('.', '')

        # If cleaned string is empty, return NaN
        if cleaned_str == '':
            cleaned_str = np.nan
        
        return float(cleaned_str) if cleaned_str else np.nan

    def clean_date(self, date_str):
        """
        Clean and convert date string to datetime format.
        """
        # Convert Farsi numbers to English
        def convert_farsi_to_english(text):
            farsi_numbers = '۰۱۲۳۴۵۶۷۸۹'
            english_numbers = '0123456789'
            translation_table = str.maketrans(farsi_numbers, english_numbers)
            return text.translate(translation_table)

        date_str = convert_farsi_to_english(date_str)

        try:
            return pd.to_datetime(date_str, errors='raise', format='%Y-%m-%d')
        except Exception:
            pass
        
        try:
            return pd.to_datetime(date_str, errors='raise', format='%d/%m/%Y')
        except Exception:
            pass
        
        try:
            return pd.to_datetime(date_str, errors='raise', format='%d-%b-%Y')
        except Exception:
            pass
        
        try:
            return pd.to_datetime(date_str, errors='raise', format='%b %d, %Y')
        except Exception:
            pass

        try:
            return pd.to_datetime(date_str, errors='raise', format='%d-%m-%Y')
        except Exception:
            pass
        
        try:
            return pd.to_datetime(date_str, errors='raise', format='%Y%m%d')
        except Exception:
            pass
        
        return pd.NaT  # Return NaT if no format matches

    def convert_to_jalali(self, date_gregorian):
        """
        Convert Gregorian date to Jalali (Shamsi) date.
        """
        if pd.isna(date_gregorian):
            return np.nan
        return jdatetime.date.fromgregorian(date=date_gregorian).strftime("%Y-%m-%d")
    
    def apply_clean_number(self, column_name):
        """
        Apply clean_number method to a specific column.
        """
        self.df[column_name] = self.df[column_name].apply(self.clean_number)
        return self.df

    def apply_clean_date(self, column_name):
        """
        Apply clean_date method to a specific column.
        """
        self.df[column_name] = self.df[column_name].apply(self.clean_date)
        return self.df

    def apply_convert_to_jalali(self, column_name):
        """
        Apply convert_to_jalali method to a specific column.
        """
        # First, make sure the column is converted to datetime if not already
        self.df[column_name] = pd.to_datetime(self.df[column_name], errors='coerce')
        
        # Then convert the Gregorian date to Jalali
        self.df[column_name] = self.df[column_name].apply(self.convert_to_jalali)
        return self.df

    def get_data(self):
        """
        Return the cleaned dataframe.
        """
        return self.df
