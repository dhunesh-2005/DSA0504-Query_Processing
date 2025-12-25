#30
import matplotlib.pyplot as plt
import numpy as np

# Sample data
men_scores = [22, 30, 35, 35, 26]
women_scores = [25, 32, 30, 35, 29]

# Groups
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
x = np.arange(len(groups))
width = 0.35

# Create bar chart
plt.bar(x - width/2, men_scores, width, label='Men', color='green')
plt.bar(x + width/2, women_scores, width, label='Women', color='red')

# Labels and title
plt.xlabel("Group")
plt.ylabel("Scores")
plt.title("Scores by Person")
plt.xticks(x, groups)
plt.legend()

# Display chart
plt.show()
