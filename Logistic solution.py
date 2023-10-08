import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Define the variable x
x = symbols('x')

# Define the two functions
y1 = x
y2 = 3.3 * x * (1 - x)

# Create an equation for the intersection points
intersection_eq = Eq(y1, y2)

# Solve for the intersection points
intersection_points = solve(intersection_eq, x)

# Convert the intersection points to numerical values
intersection_x_values = [float(point) for point in intersection_points]
intersection_y_values = [y1.subs(x, point) for point in intersection_points]

# Generate x values for the plot
x_values = np.linspace(0, 1, 100)
y1_values = x_values
y2_values = 3.3 * x_values * (1 - x_values)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label='y = x', color='red')
plt.plot(x_values, y2_values, label='y = 3.3x(1-x)', color='green')
plt.scatter(intersection_x_values, intersection_y_values, color='black', label='Intersection')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Save the plot as an image
plt.savefig('intersection_plot.png')
plt.show()
