import pandas as pd
import matplotlib.pyplot as plt

# Load and process data
df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/INT375 project/sales_data_sample.csv", encoding="latin1")
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors='coerce')

# Compute sales metrics
yearly_sales = df.groupby("YEAR_ID")["SALES"].sum()
monthly_sales = df.groupby("MONTH_ID")["SALES"].sum()

# Plot sales trends
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
yearly_sales.plot(marker='o', ax=axes[0], title="Yearly Sales")
monthly_sales.plot(kind='bar', ax=axes[1], title="Monthly Sales")
plt.show()

print(f"Total Revenue: ${df['SALES'].sum():,.2f}")
