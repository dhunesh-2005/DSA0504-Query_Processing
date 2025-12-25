#20
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Country': ['India', 'Indonesia', 'Canada', 'Ireland', 'Finland']
})

# Find index of rows containing substring 'Ind'
index_result = df[df['Country'].str.contains('Ind')].index

print(index_result)
