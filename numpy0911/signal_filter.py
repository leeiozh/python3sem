import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=1, ncols=2)

input_data = np.loadtxt("signal03.dat")
output_data = np.empty(len(input_data))

output_data[9:] = (input_data[:-9] + input_data[1:-8] + input_data[2:-7] + input_data[3:-6] + input_data[4:-5] +
                   input_data[5:-4] + input_data[6:-3] + input_data[7:-2] + input_data[8:-1] + input_data[9:]) / 9
output_data[:9] = [np.mean(input_data[0: i + 1]) for i in range(9)]

axs[0].plot(np.arange(0, len(input_data)), input_data)
axs[0].set_title("Сырой сигнал")
axs[1].plot(np.arange(0, len(output_data)), output_data)
axs[1].set_title("Фильтрованный сигнал")

axs[0].grid()
axs[1].grid()
figure = plt.gcf()
figure.set_size_inches(18, 6)
plt.savefig("signal03_filter.png")
