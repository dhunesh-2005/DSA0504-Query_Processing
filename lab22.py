import matplotlib.pyplot as plt

# Data for plotting
x = [0, 10, 20, 30, 40, 50]
y = [0, 30, 60, 90, 120, 150]

# Draw line
plt.plot(x, y)

# Add labels and title
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.title("Draw a Line")

# Display graph
plt.show()
