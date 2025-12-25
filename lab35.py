#35
import matplotlib.pyplot as plt

# Sample data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Scatter plot
plt.scatter(marks_range, math_marks, color='red', label='Math marks')
plt.scatter(marks_range, science_marks, color='green', label='Science marks')

# Labels and title
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.title("Scatter Plot of Math vs Science Marks")
plt.legend()

# Display plot
plt.show()
