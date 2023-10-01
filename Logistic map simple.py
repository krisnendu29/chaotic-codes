import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r_values = np.linspace(0.5, 4.0, 500)  # Range of 'r' values
x0 = 0.1  # Initial population value
num_iterations = 50

# Create a figure with a black background
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, num_iterations)
ax.set_ylim(0, 1)

# Set the background color of both the figure and axes to black
fig.set_facecolor('black')
ax.set_facecolor('black')

# Initialize empty arrays for data
x_values = []
y_values = []

# Initialize the plot with a cyan line
line, = ax.plot([], [], lw=2, color='cyan')  # Set the line color to cyan

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot
def update(frame):
    ax.set_title(f'r = {r_values[frame]:.2f}')

    r = r_values[frame]
    x = x0

    x_values.clear()
    y_values.clear()

    for _ in range(num_iterations):
        y = logistic_map(r, x)

        x_values.append(_)
        y_values.append(y)

        x = y

    line.set_data(x_values, y_values)
    return line,

# Create the animation with a faster interval (e.g., 10 milliseconds)
ani = FuncAnimation(fig, update, frames=len(r_values), init_func=init, blit=True, interval=10)

# Save the animation as a GIF
ani.save('logistic_map_animation.gif', writer='pillow')

# Show the animation (optional)
plt.show()
