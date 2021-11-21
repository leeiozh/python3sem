import numpy as np
import matplotlib.pyplot as plt

input_data = np.loadtxt("large.txt")
A = input_data[:-1, :]
b = input_data[-1, :]

x = np.linalg.solve(A, b)

plt.bar(np.arange(x.shape[0]), x)
plt.grid()
plt.savefig("ep2_result.png")