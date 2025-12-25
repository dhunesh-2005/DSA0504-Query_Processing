
#23
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# STEP 1: Create the 'test.txt' file
# (This part creates the file for you automatically)
with open('test.txt', 'w') as f:
    f.write("1 2\n")
    f.write("2 4\n")
    f.write("3 1\n")
# ---------------------------------------------------------

# STEP 2: Read data from the file
x_values = []
y_values = []

# Open the file and read line by line
with open('test.txt', 'r') as f:
    for line in f:
        # Split the line into two parts (x and y)
        parts = line.split()
        if len(parts) == 2:
            x_values.append(float(parts[0]))
            y_values.append(float(parts[1]))

# STEP 3: Draw the line
plt.plot(x_values, y_values)

# STEP 4: Add Labels and Title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')

# STEP 5: Display the graph
# In IDLE, this command will pop up a new window with the graph
plt.show()
