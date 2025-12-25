import pandas as pd
import numpy as np

# 1. Create a DataFrame with 10 rows and 4 columns of random values
# Using np.random.randn to generate standard normal distribution values
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# 2. Define a function or use set_properties to apply the style
# 'background-color' sets the cell background
# 'color' sets the font color
styled_df = df.style.set_properties(**{
    'background-color': 'black',
    'color': 'yellow',
    'border-color': 'white' # Optional: adds a border to make cells distinct
})

# 3. Display the dataframe (This renders the style in Jupyter/Colab)
styled_df
