import pandas as pd
import numpy as np
import jdatetime
import re

from streamlit import dataframe


class cleaner:
    def __init__(self,df):
        self.df = df

    def to_float_number(self,col,clean_col):

        def convert(x):
            if x is None:
                return None
            s = str(x).strip()
            if s == "":
                return None
            if s.isdigit():
                return float(s)
            cleaned = re.sub(r"[^0-9.]", "", s)
            return float(cleaned) if cleaned else None

        self.df[clean_col] = self.df[col].apply(lambda v: convert(v))
        return    self.df
        
    def to_miladi(self,col,clean_col):
            
        def convert_farsi_to_english(date):
            farsi_numbers = '۰۱۲۳۴۵۶۷۸۹'
            english_numbers = '0123456789'
            translation_table = str.maketrans(farsi_numbers, english_numbers)
            return date.translate(translation_table)
        
        date_formats = [
            "%b %d, %Y",  # Jan 01, 2023
            "%Y-%m-%d",   # 2023-01-01
            "%d/%m/%Y",   # 01/01/2023
            "%d-%b-%Y",   # 01-Jan-2023
            "%d-%m-%Y",   # 01-01-2023
            "%d %m %Y",   # 01 01 2023
            "%Y%m%d",     # 20230101
            "%m/%d/%Y",   # 01/25/2023
            "%d.%m.%Y",   # 25.01.2023
            "%Y/%m/%d",   # 2023/01/25
            "%d-%b-%Y"    
        ]


        def convert_to_date(x):
            x = convert_farsi_to_english(x).strip()
            for fmt in date_formats:
                try:
                    return pd.to_datetime(x, format=fmt)
                except:
                    continue

            try:
                return pd.to_datetime(x, errors='coerce')
            except:
                return np.nan


        self.df[clean_col] = self.df[col].apply(lambda v: convert_farsi_to_english(v))
        self.df[clean_col] = self.df[col].apply(lambda x : convert_to_date(x))
        return self.df
        
    def to_shamsi(self,col):
        return 2
    

    
    def season_from_date(self,col,clean_col):
        def season(x):
            
            if x.month in [12, 1, 2]:
                return "Winter"
            elif x.month in [3, 4, 5]:
                return "Spring"
            elif x.month in [6, 7, 8]:
                return "Summer"
            elif x.month in [9, 10, 11]:
                return "Autumn"
            elif x is np.nan:
                return np.nan
            

        self.df[clean_col] = self.df[col].apply(lambda m: season(m))
        return self.df