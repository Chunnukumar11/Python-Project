import pandas as pd


df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/INT375 project/sales_data_sample.csv", encoding="latin1")

total_revenue = df["SALES"].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")

