#24
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------------
# STEP 1: Create the 'fdata.csv' file
# (Run this once to create the file with the data from the question)
csv_data = """Date,Open,High,Low,Close
10-03-16,774.25,776.065002,769.5,772.559998
10-04-16,776.030029,778.710022,772.890015,776.429993
10-05-16,779.309998,782.070007,775.650024,776.469971
10-06-16,779.78047998,775.539978,776.859985,776.859985
10-07-16,779.659973,779.659973,770.75,775.080017
"""

with open('fdata.csv', 'w') as f:
    f.write(csv_data)
# ---------------------------------------------------------

# STEP 2: Read the data using Pandas
df = pd.read_csv('fdata.csv')

# STEP 3: Plot the lines
# We plot 'Date' on the x-axis and the other columns on the y-axis
plt.plot(df['Date'], df['Open'], label='Open')
plt.plot(df['Date'], df['High'], label='High')
plt.plot(df['Date'], df['Low'], label='Low')
plt.plot(df['Date'], df['Close'], label='Close')

# STEP 4: Add Title, Labels, and Legend
plt.xlabel('Date')
plt.ylabel('Financial Values')
plt.title('Alphabet Inc. Financial Data (Oct 2016)')
plt.legend()  # This adds the small box showing which color is which

# STEP 5: Display the graph
plt.show()
