import pandas as pd

# 1. Create the data manually based on your screenshot
data = {
    'Region': [
        'East', 'Central', 'Central', 'Central', 'West',
        'East', 'Central', 'Central', 'West', 'East',
        'Central', 'East', 'East', 'East', 'Central',
        'East', 'Central', 'East'
    ],
    'Manager': [
        'Martha', 'Hermann', 'Hermann', 'Timothy', 'Timothy',
        'Martha', 'Martha', 'Hermann', 'Douglas', 'Martha',
        'Hermann', 'Martha', 'Douglas', 'Martha', 'Douglas',
        'Martha', 'Hermann', 'Martha'
    ],
    'SalesMan': [
        'Alexander', 'Shelli', 'Luis', 'David', 'Stephen',
        'Alexander', 'Steven', 'Luis', 'Michael', 'Alexander',
        'Sigal', 'Diana', 'Karen', 'Alexander', 'John',
        'Alexander', 'Sigal', 'Alexander'
    ],
    'Sale_amt': [
        113810.00, 25000.00, 43128.00, 6075.00, 67088.00,
        30000.00, 89850.00, 107820.00, 38336.00, 30000.00,
        107820.00, 14500.00, 40500.00, 41930.00, 250.00,
        936.00, 14000.00, 14400.00
    ]
}

# 2. Convert dictionary to DataFrame
df = pd.DataFrame(data)

# 3. Create pivot table
# This sums up sales amounts by Region, then Manager, then SalesMan
pivot = pd.pivot_table(
    df,
    index=['Region', 'Manager', 'SalesMan'],
    values='Sale_amt',
    aggfunc='sum'
)

# 4. Print the result
print(pivot)
