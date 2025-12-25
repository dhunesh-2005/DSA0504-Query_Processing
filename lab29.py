
#29
import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Colors for each bar
colors = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']

# Create bar chart with different colors
plt.bar(languages, popularity, color=colors)

# Labels and title
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")

# Display chart
plt.show()
