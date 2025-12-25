import pandas as pd

# 1. Create the data manually (instead of reading CSV)
data = {
    'item': ['Television', 'Fridge', 'Television', 'Microwave', 'Fridge', 'Microwave', 'Television'],
    'units_sold': [10, 5, 15, 8, 3, 4, 12]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Create pivot table for item-wise units sold
# aggfunc='sum' adds up all the units for each specific item
pivot = pd.pivot_table(
    df,
    index='item',
    values='units_sold',
    aggfunc='sum'
)

# 4. Print the result
print(pivot)
