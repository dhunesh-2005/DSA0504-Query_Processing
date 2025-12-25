import pandas as pd

# 1. Create the data manually instead of reading a CSV
data = {
    'item': ['Television', 'Fridge', 'Television', 'Microwave', 'Fridge', 'Microwave', 'Television', 'Fridge'],
    'sale_value': [1500, 800, 1550, 200, 850, 220, 1450, 900]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Create pivot table
# This finds the Maximum and Minimum sale value for each distinct item
pivot = pd.pivot_table(
    df,
    index='item',
    values='sale_value',
    aggfunc=['max', 'min']
)

# 4. Print the result
print(pivot)
