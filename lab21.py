#21
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes']
})

print("Original DataFrame:")
print(df)

# Swap case ONLY for the row at index 1
# df.at[row_index, column_name] allows you to modify a single value
df.at[1, 'Name'] = df.at[1, 'Name'].swapcase()

print("\nDataFrame after swapping index 1:")
print(df)
