
#25
import matplotlib.pyplot as plt

# X-axis values
x = [10, 20, 30]

# Y-axis values for two lines
y1 = [20, 35, 10]
y2 = [40, 10, 30]

# Plot lines with different colors and widths
plt.plot(x, y1, color='blue', linewidth=3, label='Line 1 (width=3)')
plt.plot(x, y2, color='red', linewidth=5, label='Line 2 (width=5)')

# Labels and title
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.title("Two or more lines with different widths and colors")

# Legend
plt.legend()

# Display plot
plt.show()
