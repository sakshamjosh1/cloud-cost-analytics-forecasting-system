import pandas as pd
import numpy as np

# reproducible random values
np.random.seed(42)

# create date range for 1 year
dates = pd.date_range(start="2025-01-01", periods=365, freq="D")

# generate service costs
ec2 = 50 + np.random.normal(0, 5, 365) + np.linspace(0, 10, 365)
s3 = 10 + np.linspace(0, 8, 365) + np.random.normal(0, 1, 365)
rds = 20 + np.random.normal(0, 2, 365)
lambda_cost = 5 + np.random.normal(0, 2, 365)

# add random spikes
for i in np.random.choice(range(365), 10, replace=False):
    ec2[i] += np.random.randint(15, 35)

# create dataframe
df = pd.DataFrame({
    "Date": dates,
    "EC2_Cost": ec2,
    "S3_Cost": s3,
    "RDS_Cost": rds,
    "Lambda_Cost": lambda_cost
})

# total cost
df["Total_Cost"] = df["EC2_Cost"] + df["S3_Cost"] + df["RDS_Cost"] + df["Lambda_Cost"]

# round values
df = df.round(2)

# save csv
df.to_csv("cloud_billing_data.csv", index=False)

print(df.head())