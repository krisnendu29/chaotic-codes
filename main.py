import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the logistic equation function
def logistic_equation(r, x):
    return r * x * (1 - x)

# Number of iterations for each value of r
num_iterations = 1000

# Number of values for r and their range
num_r_values = 1000
r_values = np.linspace(0, 4, num_r_values)

# Create an array to store the x values for each r
x_values = np.empty((num_r_values, num_iterations))

# Initial condition
x0 = 0.5

# Iterate through different values of r and store the results
for i in range(num_r_values):
    r = r_values[i]
    x = x0
    for j in range(num_iterations):
        x = logistic_equation(r, x)
        x_values[i, j] = x

# Create a function to initialize the plot
def init():
    ax.set_title("Bifurcation Diagram of the Logistic Equation")
    ax.set_xlabel("r")
    ax.set_ylabel("Steady-State Values of x")
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 1)
    scatter.set_sizes([10])  # Increase marker size
    scatter.set_color('blue')  # Marker color
    return scatter,

# Create a function to update the plot for each frame of the animation
def update(frame):
    scatter.set_offsets(np.column_stack((r_values, x_values[:, frame])))
    return scatter,

# Create the animation
fig, ax = plt.subplots(figsize=(12, 6))
scatter = ax.scatter([], [], s=10, c='blue', marker='.')
animation = FuncAnimation(fig, update, frames=num_iterations, init_func=init, blit=True)

# Save the animation as a GIF file
animation.save('bifurcation_animation.gif', writer='pillow', fps=30)

# HTML code to embed the GIF in a web page
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Bifurcation Animation</title>
</head>
<body>
    <img src="bifurcation_animation.gif" width="800" height="400" />
</body>
</html>
"""

# Save the HTML code to a file
with open('bifurcation_animation.html', 'w') as html_file:
    html_file.write(html_code)

plt.show()
