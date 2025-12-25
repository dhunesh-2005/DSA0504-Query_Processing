import pandas as pd
import matplotlib.pyplot as plt

# 1. Read stock data
df = pd.read_csv("alphabet_stock_data.csv")

# 2. Convert Date column (FIXED: Added dayfirst=True to handle dd-mm-yyyy format)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# 3. Filter between dates (YYYY-MM-DD format is standard for filtering)
start_date = '2020-04-01'
end_date = '2020-05-01'

# Filter the data
data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# 4. Create Scatter plot (Price vs Volume)
plt.figure(figsize=(10, 6)) # Optional: Makes the chart bigger and easier to read
plt.scatter(data['Close'], data['Volume'], color='blue', alpha=0.5)

# 5. Add Labels and Title
plt.xlabel("Closing Price ($)")
plt.ylabel("Trading Volume")
plt.title("Alphabet Inc. Price vs Volume")
plt.grid(True) # Adds a grid to make it look professional

# 6. Show the plot
plt.show()
