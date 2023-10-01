import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.colors import Normalize

# Define the Lorenz system of differential equations
def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Set the Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Set the initial conditions and time span for integration
initial_state = [1.0, 0.0, 0.0]
t_span = (0, 100)
t_eval = np.linspace(*t_span, 10000)

# Solve the Lorenz system using solve_ivp
solution = solve_ivp(lorenz, t_span, initial_state, args=(sigma, rho, beta), t_eval=t_eval)

# Extract the solution data
x, y, z = solution.y

# Create a normalized time array for coloring the trajectory
norm = Normalize(t_eval.min(), t_eval.max())
colors = plt.cm.viridis(norm(t_eval))

# Create a 3D plot of the multicolored Lorenz attractor with a black background
fig = plt.figure(figsize=(8, 8), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')
for i in range(len(x) - 1):
    ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=colors[i], lw=1, alpha=0.6)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot title
ax.set_title('Multicolored Lorenz Attractor', color='white')

# Create a colorbar for reference
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, label='Time')

# Save the plot as an image in PNG format
plt.savefig('multicolored_lorenz.png', bbox_inches='tight', pad_inches=0, dpi=300)

# Display the plot
plt.show()
