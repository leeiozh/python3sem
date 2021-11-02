import matplotlib.pyplot as plt
import os

number_of_datas = 5

fig, axs = plt.subplots(nrows=1, ncols=number_of_datas)

x = [[] for i in range(number_of_datas)]
y = [[] for i in range(number_of_datas)]

for i in range(number_of_datas):
    with open(os.path.join("data", "00" + str(i + 1) + ".dat"), 'r') as file:
        for line in file:
            count = float(line.split()[0])
            break
        for line in file:
            if count <= 0:
                break
            else:
                count -= 1
                y[i].append(float(line.split()[1]))
                x[i].append(float(line.split()[0]))
    axs[i].scatter(x[i], y[i], s=3)

plt.axis('equal')

figure = plt.gcf()
figure.set_size_inches(18, 6)
plt.savefig("dead.png")
