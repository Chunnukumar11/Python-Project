import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/INT375 project/sales_data_sample.csv", encoding="latin1")
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors='coerce')

# Sales metrics
total_revenue = df["SALES"].sum()
yearly_sales = df.groupby("YEAR_ID")["SALES"].sum()

# Plot
yearly_sales.plot(marker='o', title="Yearly Sales")
plt.show()

print(f"Total Revenue: ${total_revenue:,.2f}")

