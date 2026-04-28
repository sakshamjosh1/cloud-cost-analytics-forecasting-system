import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os

os.makedirs("outputs/charts", exist_ok=True)

# load dataset
df = pd.read_csv("data/cloud_billing_data.csv")

# convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# first 5 rows
print(df.head())

# dataset shape
print("Rows, Columns:", df.shape)

# datatypes
print(df.info())

# null values
print(df.isnull().sum())

# summary statistics
print(df.describe())



# Data Visualization

# -------------------------------
# 1. Daily Total Cost Trend
# -------------------------------
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Total_Cost"])
plt.title("Daily Total Cloud Cost")
plt.xlabel("Date")
plt.ylabel("Cost")
plt.grid(True)
plt.savefig("outputs/charts/daily_trend.png")
plt.close()

# -------------------------------
# 2. Monthly Total Cost
# -------------------------------
monthly_cost = df.resample("ME", on="Date")["Total_Cost"].sum()

plt.figure(figsize=(10,5))
monthly_cost.plot(kind="bar")
plt.title("Monthly Cloud Spending")
plt.xlabel("Month")
plt.ylabel("Total Cost")
plt.tight_layout()
plt.savefig("outputs/charts/monthly_spending.png")
plt.close()

# -------------------------------
# 3. Average Cost by Service
# -------------------------------
avg_services = df[["EC2_Cost","S3_Cost","RDS_Cost","Lambda_Cost"]].mean()

plt.figure(figsize=(8,5))
avg_services.plot(kind="bar")
plt.title("Average Cost by Service")
plt.xlabel("Service")
plt.ylabel("Average Daily Cost")
plt.tight_layout()
plt.savefig("outputs/charts/service_cost.png")
plt.close()


# -------------------------------
# Basic Statistics
# -------------------------------

print("\n--- Statistical Analysis ---")

# Mean
print("Average Daily Total Cost:", round(df["Total_Cost"].mean(), 2))

# Median
print("Median Daily Total Cost:", round(df["Total_Cost"].median(), 2))

# Standard Deviation
print("Std Deviation:", round(df["Total_Cost"].std(), 2))

# Highest Spending Day
max_row = df.loc[df["Total_Cost"].idxmax()]
print("\nHighest Spending Day:")
print(max_row[["Date", "Total_Cost"]])

# Lowest Spending Day
min_row = df.loc[df["Total_Cost"].idxmin()]
print("\nLowest Spending Day:")
print(min_row[["Date", "Total_Cost"]])

# Correlation Matrix
print("\nCorrelation Matrix:")
print(df[["EC2_Cost","S3_Cost","RDS_Cost","Lambda_Cost","Total_Cost"]].corr())

# -------------------------------
# 7-Day Moving Average
# -------------------------------

df["7D_MA"] = df["Total_Cost"].rolling(window=7).mean()

plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Total_Cost"], label="Actual Cost")
plt.plot(df["Date"], df["7D_MA"], label="7-Day Moving Average", linewidth=2)
plt.title("Cloud Cost vs 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Cost")
plt.legend()
plt.grid(True)
plt.savefig("outputs/charts/7_Moving_Avg.png")
plt.close()


# -------------------------------
# ARIMA Forecast
# -------------------------------

model = ARIMA(df["Total_Cost"], order=(1,1,1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=30)

print("\nNext 30 Days Forecast:")
print(forecast)

# -------------------------------
# SQL Integration (SQLite)
# -------------------------------
import sqlite3

# create connection
conn = sqlite3.connect("cloud_cost.db")

# load dataframe into SQL table
df.to_sql("billing", conn, if_exists="replace", index=False)

print("\nData successfully stored in SQLite database.")

# run SQL query
query = """
SELECT substr(Date,1,7) as Month, SUM(Total_Cost) as Total
FROM billing
GROUP BY Month
ORDER BY Month;
"""

result = pd.read_sql_query(query, conn)

print("\nMonthly Cost using SQL:")
print(result)

# close connection
conn.close()