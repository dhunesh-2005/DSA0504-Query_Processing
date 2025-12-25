import pandas as pd

# 1. Create the DataFrame manually with the data from your image
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [1.32921, -1.07082, -1.6264, 0.961538, 1.45342,
          -1.33694, 0.121668, 0.354493, 1.69858, -0.12982],
    'C': [-0.770033, -1.43871, 0.219565, 0.104011, 1.05774,
          0.562861, 1.2076, 1.03753, -1.32596, 0.631523],
    'D': [-0.31628, 0.564417, 0.678805, -0.481165, 0.165562,
          1.39285, -0.00204021, -0.385684, 1.42898, -0.586538],
    'E': [-0.99081, 0.295722, 1.88927, 0.850229, 0.515018,
          -0.063328, 1.6278, 0.519818, -2.08935, 0.29072]
}

df = pd.DataFrame(data)

# 2. Define the styling function (Red for negative, Black for positive)
def color_values(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# 3. Apply the styling
# Note: In newer pandas versions, .map() is preferred over .applymap()
styled_df = df.style.map(color_values)

# 4. Save to HTML to verify the colors
# Open 'output.html' in your folder to see the red numbers
styled_df.to_html("styled_output.html")

print("Success! Open 'styled_output.html' to see the colored table.")
print("Here is the plain text data:")
print(df)
