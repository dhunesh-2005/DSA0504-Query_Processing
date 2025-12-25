#31
import matplotlib.pyplot as plt
import numpy as np

# Sample data
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]

men_std = [4, 3, 4, 1, 5]
women_std = [3, 5, 2, 3, 3]

# Groups
groups = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
x = np.arange(len(groups))
width = 0.5

# Plot stacked bars
plt.bar(x, men_means, width, yerr=men_std, label='Men', color='red')
plt.bar(x, women_means, width, bottom=men_means,
        yerr=women_std, label='Women', color='green')

# Labels and title
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Scores by group and gender")
plt.xticks(x, groups)
plt.legend()

# Display plot
plt.show()
