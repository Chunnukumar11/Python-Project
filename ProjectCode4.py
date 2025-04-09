import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Parse date column
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df.dropna(subset=['ORDERDATE'], inplace=True)

# Extract temporal features
df['YEAR'] = df['ORDERDATE'].dt.year
df['MONTH'] = df['ORDERDATE'].dt.month
df['QUARTER'] = df['ORDERDATE'].dt.quarter
df['YearMonth'] = df['ORDERDATE'].dt.to_period('M')

# Monthly trend
monthly_sales = df.groupby('YearMonth')['SALES'].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot(marker='o', color='darkblue')
plt.title('Monthly Sales Trend')
plt.xlabel('Year-Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# Yearly trend
yearly_sales = df.groupby('YEAR')['SALES'].sum()
plt.figure(figsize=(8, 5))
sns.barplot(x=yearly_sales.index, y=yearly_sales.values, palette='crest', legend=False)
plt.title('Yearly Sales Trend')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Monthly average sales across years
avg_monthly = df.groupby('MONTH')['SALES'].mean()
plt.figure(figsize=(10, 5))
sns.lineplot(x=avg_monthly.index, y=avg_monthly.values, marker='o', color='green')
plt.title('Average Sales by Month')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.xticks(range(1,13))
plt.grid(True)
plt.tight_layout()
plt.show()

# Quarterly trend
quarterly_sales = df.groupby(['YEAR', 'QUARTER'])['SALES'].sum().unstack()
quarterly_sales.plot(kind='bar', stacked=True, figsize=(10,6), colormap='Paired')
plt.title('Quarterly Sales by Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
