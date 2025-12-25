#36
import matplotlib.pyplot as plt

# Data for three groups
weight_group1 = [55, 58, 60, 62, 65]
height_group1 = [120, 135, 150, 155, 165]

weight_group2 = [60, 63, 66, 68, 70]
height_group2 = [140, 155, 165, 175, 185]

weight_group3 = [58, 61, 64, 67, 72]
height_group3 = [125, 145, 155, 170, 190]

# Scatter plots
plt.scatter(weight_group1, height_group1, color='blue', label='Group 1')
plt.scatter(weight_group2, height_group2, color='green', label='Group 2')
plt.scatter(weight_group3, height_group3, color='red', label='Group 3')

# Labels and title
plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Group wise Weight vs Height scatter plot")
plt.legend()

# Display plot
plt.show()
