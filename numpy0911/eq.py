import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

input_data = np.loadtxt("start.dat")
size = len(input_data)
output_data = np.zeros((255, size))
output_data[0] = input_data

A = np.eye(size)
A[size - 1, 0] = -1
for i in range(1, size):
    A[i, i - 1] = -1

for i in range(1, size):
    output_data[i] = output_data[i - 1] - 0.5 * np.dot(A, output_data[i - 1])

fig = plt.figure()
ax = plt.axes()
line, = ax.plot(np.arange(0, 50), input_data)


def init():
    line.set_ydata(input_data)
    return line,


def animate(i):
    line.set_ydata(output_data[i])
    return line,


anim = FuncAnimation(fig, animate, frames=255, init_func=init, interval=1, blit=True)
anim.save('eq.gif', writer='imagemagick')
