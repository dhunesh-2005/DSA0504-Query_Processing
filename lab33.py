#33
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.randn(50)
y = np.random.randn(50)

# Create scatter plot with empty circles
plt.scatter(x, y, facecolors='none', edgecolors='green')

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Empty Circles")

# Display plot
plt.show()
