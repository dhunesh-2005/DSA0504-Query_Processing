#18
import pandas as pd

data = {
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
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
# Group by school_code and class
grouped = df.groupby(['school_code', 'class'])

# Display groups
for key, group in grouped:
    print("\nGroup:", key)
    print(group)

