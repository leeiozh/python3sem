import matplotlib.pyplot as plt

number_of_datas = 5

fig, axs = plt.subplots(nrows=1, ncols=number_of_datas)

x = [[] for i in range(number_of_datas)]
y = [[] for i in range(number_of_datas)]

for i in range(number_of_datas):
    with open("data/00" + str(i + 1) + ".dat", 'r') as file:
        for line in file:
            try:
                y[i].append(float(line.split()[1]))
                x[i].append(float(line.split()[0]))
            except:
                pass
    axs[i].scatter(x[i], y[i], s=3)

plt.axis('equal')

figure = plt.gcf()
figure.set_size_inches(18, 6)
plt.savefig("dead.png")
