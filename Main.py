from DataCleaner.py import DataLoader
from DataLoader.py import DataLoader

data_loader = DataLoader(r'C:\Users\amir\Downloads\amazon_products.csv')
df = data_loader.get_data()

# Initialize DataCleaner and clean the data
data_cleaner = DataCleaner(df)

# Apply cleaning functions to specific columns (e.g., 'price' and 'date')
df = data_cleaner.apply_clean_number('actual_price')
df = data_cleaner.apply_clean_number('discount_price')
df = data_cleaner.apply_clean_number('ratings')
df = data_cleaner.apply_clean_number('no_of_ratings')
df = data_cleaner.apply_clean_date('date')
df = data_cleaner.apply_convert_to_jalali('date')

# Print cleaned dataframe
df.info()