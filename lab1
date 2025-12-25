import pandas as pd

# Load the csv file
df = pd.read_csv('employees.csv')

# Select both columns and drop duplicate rows to get unique pairs
result = df['DEPARTMENT_ID'].drop_duplicates()

print("Distinct Departments:")
print(result)
