import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Define the variable x
x = symbols('x')

# Define the three functions
y1 = x
y2 = 3.3 * x * (1 - x)
y3 = 3.3 * (3.3 * x * (1 - x)) * (1 - 3.3 * x * (1 - x))

# Create an equation for the intersection points of y1 and y2
intersection_eq12 = Eq(y1, y2)

# Create an equation for the intersection points of y1 and y3
intersection_eq13 = Eq(y1, y3)

# Solve for the intersection points of y1 and y2
intersection_points12 = solve(intersection_eq12, x)

# Solve for the intersection points of y1 and y3
intersection_points13 = solve(intersection_eq13, x)

# Convert the intersection points to numerical values
intersection_x_values12 = [float(point) for point in intersection_points12]
intersection_y_values12 = [y1.subs(x, point) for point in intersection_points12]

intersection_x_values13 = [float(point) for point in intersection_points13]
intersection_y_values13 = [y1.subs(x, point) for point in intersection_points13]

# Generate x values for the plot
x_values = np.linspace(0, 1, 100)
y1_values = x_values
y2_values = 3.3 * x_values * (1 - x_values)
y3_values = 3.3 * (3.3 * x_values * (1 - x_values)) * (1 - 3.3 * x_values * (1 - x_values))

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label='y = x', color='blue', linewidth=2, linestyle='-', markersize=4, markerfacecolor='blue', markeredgecolor='black')
plt.plot(x_values, y2_values, label='y = 3.3x(1-x) = f(x)', color='red', linewidth=2, linestyle='-', markersize=4, markerfacecolor='red', markeredgecolor='black')
plt.plot(x_values, y3_values, label='y = f(f(x))', color='purple', linewidth=2, linestyle='-', markersize=4, markerfacecolor='purple', markeredgecolor='black')
plt.scatter(intersection_x_values12, intersection_y_values12, color='green',  edgecolors='black', linewidths=1)
plt.scatter(intersection_x_values13, intersection_y_values13, color='orange',  edgecolors='black', linewidths=1)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Save the plot as an image
plt.savefig('intersection_plot.png')
plt.show()
