#17
import pandas as pd

data = {
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes',
             'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12]
}

df = pd.DataFrame(data)
#print(df)
#
# Group by school code and calculate mean, min, max of age
result = df.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

print(result)
