#19
import pandas as pd

# 1. Create the DataFrame matching the sample data in the image
data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("-" * 30)

# 2. Display the dimensions (shape) of the dataset
# The shape property returns a tuple representing the dimensionality (rows, columns)
print("Dimensions (Shape) of the dataset:")
print(df.shape)

# 3. Extract the column names from the dataset
# The columns property returns an Index object containing the column labels
print("\nColumn Names:")
print(df.columns)
