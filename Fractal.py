import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the Mandelbrot set
width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 256

# Create a grid of complex numbers
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
c = X + 1j * Y
z = c.copy()
output = np.zeros((height, width))

# Generate the Mandelbrot set
for i in range(max_iter):
    mask = np.abs(z) < 10
    z[mask] = z[mask] * z[mask] + c[mask]
    output += mask

# Normalize the output and create the fractal image
output = np.log(output + 1)
output = (output / np.max(output) * 255).astype(np.uint8)

# Set the background color to black
plt.figure(figsize=(8, 8), facecolor='black')

# Display the fractal with a black background
plt.imshow(output, extent=(xmin, xmax, ymin, ymax), cmap='inferno', origin='lower')
plt.colorbar()
plt.title('Mandelbrot Fractal')

# Save the fractal as an image in PNG format
plt.savefig('mandelbrot_fractal.png', bbox_inches='tight', pad_inches=0, dpi=300)
plt.show()
