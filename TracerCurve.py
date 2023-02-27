import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the range of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Create a grid of x and y values
X, Y = np.meshgrid(x, y)

# Define the multivariate function
def f(x, y, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s):
    return a*np.sin(b*x) + c*np.sin(d*y) + e*np.cos(f*x) + g*np.cos(h*y) * i*np.sin(j*x) * k*np.sin(l*y) * m*np.cos(n*x) * o*np.cos(p*y) + q*x*y + r*x**2 + s*y**2

# Define the update function for the animation
def update(frame):
    global lines

    # Remove the first line from the list and remove it from the plot
    if len(lines) > 5:
        lines[0].remove()
        lines.pop(0)

    # Calculate the function with the current coefficients for each point in the grid
    Z = f(X, Y, *coefficients)

    # Create the contour lines for the current level
    levels = np.linspace(np.min(Z), np.max(Z), 100)
    level = levels[frame]
    cs = ax.contour(X, Y, Z, levels=[level], colors='white')
    
    # Add the new contour line to the list
    lines.extend(cs.collections)
    
    # If the animation has completed one full cycle
    if frame == len(levels) - 1:
        # Choose new random coefficients for the next cycle
        for i in range(len(coefficients)):
            if np.random.rand() < 0.3:
                coefficients[i] = 0
            else:
                coefficients[i] = np.random.randint(-10, 11)
    
    return lines

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

# Set the background color to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Create an empty list to hold the contour lines
lines = []

# Choose the initial coefficients
coefficients = [np.random.choice([0, np.random.randint(-10, 11)]) for i in range(19)]

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=30, blit=True)

# Show the animation
plt.show()

