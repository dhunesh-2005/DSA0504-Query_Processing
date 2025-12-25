
import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create horizontal bar chart
plt.barh(languages, popularity)

# Labels and title
plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.title("Popularity of Programming Languages")

# Display chart
plt.show()
