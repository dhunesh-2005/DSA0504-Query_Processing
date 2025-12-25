import pandas as pd
import matplotlib.pyplot as plt

# 1. Create sample data for Alphabet Inc. (GOOGL) with Trading Volume
data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', '2023-04-05',
             '2023-04-06', '2023-04-07', '2023-04-08', '2023-04-09', '2023-04-10'],
    'Volume': [1500000, 1800000, 1600000, 1750000, 1400000,
               2000000, 2100000, 1900000, 1650000, 1550000]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Convert 'Date' to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# 4. Define the date range
start_date = '2023-04-01'
end_date = '2023-04-05'

# 5. Filter the data
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df.loc[mask]

# 6. Create the Bar Plot
plt.figure(figsize=(10, 5))

# We use plt.bar() instead of plt.plot() for bar charts
plt.bar(filtered_df['Date'], filtered_df['Volume'], color='green')

# 7. Add Labels and Title
plt.title(f'Alphabet Inc. Trading Volume ({start_date} to {end_date})')
plt.xlabel('Date')
plt.ylabel('Volume (Shares Traded)')
plt.xticks(rotation=45) # Rotates the dates so they don't overlap
plt.grid(axis='y')      # Add grid lines only for the Y-axis

# 8. Show the graph
plt.show()
