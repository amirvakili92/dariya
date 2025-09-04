from DataCleaner import DataCleaner
from DataLoader import DataLoader

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

df['month_year'] = df['date'].str[5:7]
df['discount_percentage'] = ((df['actual_price'] - df['discount_price']) / df['actual_price']) * 100
# df['monthly_sales'] = df['actual_price'] * df['no_of_ratings']

monthly_summary = df.groupby('month_year').agg(
    total_sales=('actual_price', 'sum'),  average_discount_percentage=('discount_percentage', 'mean') ).reset_index()

monthly_summary.style.format({
    'total_sales': '{:,.1f}',
    'average_discount_percentage': '{:,.1f}'
})

