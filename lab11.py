import pandas as pd
import numpy as np

# 1. Create a DataFrame with random values (10 rows, 4 columns)
# np.random.randn generates random numbers
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# 2. Convert some specific values to NaN (Simulating missing data)
df.iloc[0, 2] = np.nan  # Row 0, Column C
df.iloc[3, 3] = np.nan  # Row 3, Column D
df.iloc[4, 1] = np.nan  # Row 4, Column B
df.iloc[9, 0] = np.nan  # Row 9, Column A

# 3. Define the highlight function
def highlight_nan(val):
    # If value is NaN, set background to Red. Otherwise, no color.
    return 'background-color: red' if pd.isna(val) else ''

# 4. Apply the style
# We use .map() because .applymap() is deprecated
styled_df = df.style.map(highlight_nan)

# 5. Save the result to an HTML file
styled_df.to_html("experiment11_output.html")

print("Experiment 11 Complete!")
print("Open the file 'experiment11_output.html' in your project folder to see the red highlights.")
print("\nHere is the raw data (NaN values show as NaN):")
print(df)
