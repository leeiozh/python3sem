import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=1, ncols=2)

input_data = np.loadtxt("signal03.dat")
output_data = np.empty(len(input_data))

for i in range(len(output_data)):
    if i > 8:
        output_data[i] = np.mean(input_data[i - 9: i + 1])
    else:
        output_data[i] = np.mean(input_data[0: i + 1])

axs[0].plot(np.arange(0, len(input_data)), input_data)
axs[0].set_title("Сырой сигнал")
axs[1].plot(np.arange(0, len(output_data)), output_data)
axs[1].set_title("Фильтрованный сигнал")

axs[0].grid()
axs[1].grid()
figure = plt.gcf()
figure.set_size_inches(18, 6)
plt.savefig("signal03_filter.png")
