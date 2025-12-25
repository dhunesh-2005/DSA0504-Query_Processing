#32
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.randn(200)
y = np.random.randn(200)

# Create scatter plot
plt.scatter(x, y, color='red')

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot of Random Distribution")

# Display plot
plt.show()
