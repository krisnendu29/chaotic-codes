import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r = 3.9  # You can adjust this value to see different behaviors
x1 = 0.5
x2 = 0.51
iterations = 40

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set the background color to black

# Initialize empty lists to store trajectory data
trajectory_x1 = []
trajectory_x2 = []

# Set up the plot for both trajectories with bright colors
line_x1, = ax.plot([], [], linestyle='-', color='cyan')  # Bright cyan color
line_x2, = ax.plot([], [], linestyle='--', color='magenta')  # Bright magenta color

ax.set_xlabel('Iteration Number')
ax.set_ylabel('Iterated Output')
ax.set_xlim(0, iterations)
ax.set_ylim(0, 1)

# Function to initialize the plot
def init():
    line_x1.set_data([], [])
    line_x2.set_data([], [])
    return line_x1, line_x2

# Animation update function
def update(frame):
    global x1, x2
    trajectory_x1.append(x1)
    trajectory_x2.append(x2)
    x1 = logistic_map(r, x1)
    x2 = logistic_map(r, x2)
    line_x1.set_data(range(frame), trajectory_x1[:frame])
    line_x2.set_data(range(frame), trajectory_x2[:frame])
    return line_x1, line_x2

# Create the animation
ani = FuncAnimation(fig, update, frames=iterations, init_func=init, repeat=False)

# Save the animation as a GIF with a transparent background using PillowWriter
ani.save('butterfly_effect.gif', writer=PillowWriter(fps=30))

plt.show()
