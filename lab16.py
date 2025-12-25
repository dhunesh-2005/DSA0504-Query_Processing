#16
import pandas as pd

data = {
    'school_code': ['S001', 'S002', 'S003', 'S001', 'S002', 'S004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes',
             'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3',
                'street1', 'street2', 'street4']
}

df = pd.DataFrame(data)
#print(df)

# Group the DataFrame based on school_code
grouped = df.groupby('school_code')

# Display groups
for code, group in grouped:
    print("\nSchool Code:", code)
    print(group)

# Check the type of GroupBy object
print("\nType of GroupBy object:", type(grouped))

