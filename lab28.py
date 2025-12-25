
#28
import matplotlib.pyplot as plt

# Create a figure
plt.figure(figsize=(8, 6))

# First subplot (top)
plt.subplot(2, 1, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("First Plot")

# Second subplot (bottom-left)
plt.subplot(2, 3, 4)
plt.plot([1, 2, 3], [3, 2, 1])
plt.title("Second Plot")

# Third subplot (bottom-middle)
plt.subplot(2, 3, 5)
plt.plot([1, 2, 3], [2, 4, 6])
plt.title("Third Plot")

# Fourth subplot (bottom-right)
plt.subplot(2, 3, 6)
plt.plot([1, 2, 3], [6, 4, 2])
plt.title("Fourth Plot")

# Display all plots
plt.tight_layout()
plt.show()
