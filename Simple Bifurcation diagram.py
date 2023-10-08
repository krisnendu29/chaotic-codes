import numpy as np
import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Bifurcation diagram function
def bifurcation_diagram(r_values, x0, num_iterations, num_points):
    results = []

    for r in r_values:
        x = x0
        for _ in range(num_iterations):
            x = logistic_map(r, x)
            if _ >= num_iterations // 2:
                results.append([r, x])

    return np.array(results)

# Parameters
r_values = np.linspace(3.5440095, 3.56450020, 400)  # Range of r values
x0 = 0.5  # Initial condition
num_iterations = 1000  # Number of iterations per r value
num_points = 500  # Number of points to plot for each r value

# Generate the bifurcation diagram
bifurcation_data = bifurcation_diagram(r_values, x0, num_iterations, num_points)

# Separate the results into r_values and x_values
r_values = bifurcation_data[:, 0]
x_values = bifurcation_data[:, 1]

# Plot and save the bifurcation diagram
plt.figure(figsize=(10, 6))
plt.scatter(r_values, x_values, s=1, c='black', marker='.')
plt.xlabel('r')
plt.ylabel('x')
plt.title('Bifurcation Diagram of the Logistic Model')
plt.savefig('bifurcation_diagram.png', dpi=300)
plt.show()
