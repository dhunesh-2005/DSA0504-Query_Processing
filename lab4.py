import pandas as pd
import matplotlib.pyplot as plt

# 1. Create sample historical stock data for Alphabet Inc. (GOOGL)
data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', '2023-04-05',
             '2023-04-06', '2023-04-07', '2023-04-08', '2023-04-09', '2023-04-10'],
    'Close': [104.00, 105.50, 106.10, 105.00, 104.50,
              108.90, 109.50, 108.00, 107.50, 106.00]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Convert 'Date' column to datetime objects (Essential for plotting dates correctly)
df['Date'] = pd.to_datetime(df['Date'])

# 4. Define the start and end dates for filtering
start_date = '2023-04-01'
end_date = '2023-04-05'

# 5. Filter the data between these two dates
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df.loc[mask]

# 6. Create the Line Plot
plt.figure(figsize=(10, 5))  # Set the size of the graph
plt.plot(filtered_df['Date'], filtered_df['Close'], marker='o', color='blue', linestyle='-')

# 7. Add Title and Labels
plt.title(f'Alphabet Inc. Stock Prices ({start_date} to {end_date})')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.grid(True)  # Add a grid for better readability

# 8. Show the plot
print("Displaying plot window...")
plt.show()
