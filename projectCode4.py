import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data
file_path = "sales_data_sample.csv"  # Adjust path if needed
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['ORDERDATE'])

# Year-Month period column
df['YEAR_MONTH'] = df['ORDERDATE'].dt.to_period('M')

# Year-Month and aggregate SALES and QUANTITYORDERED
monthly_summary = df.groupby('YEAR_MONTH').agg({
    'SALES': 'sum',
    'QUANTITYORDERED': 'sum'
}).reset_index()

# Year-Month to timestamp for plotting
monthly_summary['YEAR_MONTH'] = monthly_summary['YEAR_MONTH'].dt.to_timestamp()

# plot style
sns.set(style="whitegrid")

# line plot
plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_summary, x='YEAR_MONTH', y='SALES', label='Revenue ($)', marker='o')
sns.lineplot(data=monthly_summary, x='YEAR_MONTH', y='QUANTITYORDERED', label='Sales Volume', marker='s')
plt.title('Monthly Sales Volume and Revenue Trend', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

#Histogram
plt.figure(figsize=(8, 5))
sns.histplot(monthly_summary['SALES'], bins=15, kde=True, color='skyblue')
plt.title('Distribution of Monthly Revenue', fontsize=14)
plt.xlabel('Revenue ($)')
plt.ylabel('Number of Months')
plt.grid(True)
plt.show()

# Box Plot
plt.figure(figsize=(6, 5))
sns.boxplot(y=monthly_summary['SALES'], color='lightgreen')
plt.title('Monthly Revenue - Box Plot', fontsize=14)
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.show()


# Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=monthly_summary, x='QUANTITYORDERED', y='SALES', color='orange')
plt.title('Revenue vs Sales Volume', fontsize=14)
plt.xlabel('Quantity Ordered')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.show()


