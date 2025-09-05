from DataCleaner import DataCleaner
from DataLoader import DataLoader
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

monthly_summary
correlation_ratings = df[['discount_percentage', 'ratings']].corr()
correlation_no_of_ratings = df[['discount_percentage', 'no_of_ratings']].corr()

# print("Correlation between discount_percentage and ratings:")
print(correlation_ratings)

# print("\nCorrelation between discount_percentage and no_of_ratings:")
print(correlation_no_of_ratings)

# Define the discount ranges
bins = [0, 10, 20, 30, 50, 100]
labels = ['0-10%', '10-20%', '20-30%', '30-50%', '50% and above']

# Create a new column for the discount range
df['discount_range'] = pd.cut(df['discount_percentage'], bins=bins, labels=labels, right=False)


# Compute the sales (you can choose either discount_price or actual_price)
# df['sales'] = df['discount_price'] * df['no_of_ratings']  # Assuming sales = price * number of ratings

# Group by discount range and sub_category, and calculate total sales
sales_summary = df.groupby(['discount_range', 'sub_category']).agg(
    total_sales=('discount_price', 'sum')
).reset_index()

# Sort the results to see which sub_category has the highest sales for each discount range
sales_summary_sorted = sales_summary.sort_values(by=['discount_range', 'total_sales'], ascending=[True, False])

print(sales_summary_sorted)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# فرض بر این است که دیتافریم شما به نام df است

# محاسبه نرخ تخفیف
df['discount_percentage'] = ((df['actual_price'] - df['discount_price']) / df['actual_price']) * 100

# تنظیمات ظاهری برای رسم هیستوگرام
plt.figure(figsize=(12, 6))

# رسم هیستوگرام برای تمام زیر دسته‌ها
sns.histplot(df, x='discount_percentage', hue='sub_category', bins=20, kde=True, 
             palette='Set2', edgecolor='black', multiple="stack")

# افزودن عنوان و برچسب‌ها
plt.title('Distribution of Discount Percentage by Sub Category', fontsize=16)
plt.xlabel('Discount Percentage', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# نمایش نمودار
plt.show()

monthly_sales_by_subcategory = df.groupby(['month_year', 'sub_category'])['actual_price'].sum().reset_index()

# تنظیمات ظاهری برای رسم نمودار
plt.figure(figsize=(12, 6))

# رسم نمودار خطی برای فروش ماهانه بر اساس زیر دسته
sns.lineplot(data=monthly_sales_by_subcategory, x='month_year', y='actual_price', hue='sub_category', marker='o')

# افزودن عنوان و برچسب‌ها
plt.title('Monthly Sales Trend by Sub Category', fontsize=16)
plt.xlabel('Month-Year', fontsize=12)
plt.ylabel('Total Monthly Sales', fontsize=12)

# نمایش نمودار
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


sales_pivot = df.groupby(['sub_category', 'month_year'])['actual_price'].sum().reset_index()

# heatmap ---
pivot_table = sales_pivot.pivot(index='sub_category', columns='month_year', values='actual_price').fillna(0)

# 
pivot_table_pct = pivot_table.div(pivot_table.sum(axis=0), axis=1) * 100

# Heatmap 
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table_pct, annot=True, fmt=".1f", cmap='YlGnBu')
plt.title("سهم فروش زیر‌دسته‌ها در ماه‌های مختلف (٪)")
plt.ylabel("زیر‌دسته (sub_category)")
plt.xlabel("ماه")
plt.tight_layout()
plt.show()



# رسم نمودار boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='sub_category', y='actual_price')
plt.title("توزیع قیمت واقعی (actual_price) در زیرشاخه‌های مختلف")
plt.xlabel("زیرشاخه (sub_category)")
plt.ylabel("قیمت واقعی (actual_price)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



df['day'] = df['date'].str[8:10]
actual_price = df.groupby(['day'])['actual_price'].count().reset_index()

# df


plt.figure(figsize=(14, 6))
plt.plot(actual_price['day'], actual_price['actual_price'], marker='o')
plt.title('ترند تعداد فروش روزانه')
plt.xlabel('روز')
plt.ylabel('تعداد فروش (count)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
