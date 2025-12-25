#14
import pandas as pd
import numpy as np

# 1. Create the DataFrame with the mixed missing indicators (?, --) from Image 14
data = {
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, "--", 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, "?", 12.43, 2480.4, 250.45, 3045.6],
    'ord_date': ["?", "2012-09-10", np.nan, "2012-08-17", "2012-09-10", "2012-07-27", "2012-09-10", "2012-10-10", "2012-10-10", "2012-06-27", "2012-08-17", "2012-04-25"],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, "--", 3002, 3001, 3001],
    'salesman_id': [5002, 5003, "?", 5001, np.nan, 5002, 5001, "?", 5003, 5002, 5003, "--"]
}

df = pd.DataFrame(data)

# 2. Define the list of formats that represent "no valuable information"
missing_value_formats = ["?", "--"]

# 3. Replace these formats with standard NaN (Not a Number)
# We use regex=False to ensure we match the exact strings
df_cleaned = df.replace(missing_value_formats, np.nan)

print("Original DataFrame (with ? and --):")
print(df)
print("\nCleaned DataFrame (Non-standard values replaced with NaN):")
print(df_cleaned)
