#34
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(20)
y = np.random.rand(20)

# Generate random sizes
sizes = np.random.randint(50, 500, size=20)

# Scatter plot with different sizes
plt.scatter(x, y, s=sizes, c=sizes, alpha=0.7)

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Different Ball Sizes")

# Display plot
plt.show()
