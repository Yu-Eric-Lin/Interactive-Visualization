import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.sin(x)

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the data
line, = ax.plot(x, y, color='blue', animated=True)

# Define a function to update the plot
def update(num):
    line.set_ydata(np.sin(x + num/10.0))  # Update the y-data
    return line,

# Use FuncAnimation to animate the plot
from matplotlib.animation import FuncAnimation
ani = FuncAnimation(fig, update, frames=100, interval=20, blit=True)

# Show the plot
plt.show()
