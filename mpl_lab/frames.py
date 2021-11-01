import matplotlib.pyplot as plt

x = []

with open("data.dat", 'r') as file:
    for i, line in enumerate(file):
        x.append([float(num) for num in line.split()])

for i in range(0, len(x), 2):
    fig, ax = plt.subplots()
    ax.plot(x[i], x[i + 1])
    ax.set_xlim(0, 16)
    ax.set_ylim(-9, 12)
    ax.grid()
    plt.savefig("frame" + str(i // 2 + 1) + ".png")
