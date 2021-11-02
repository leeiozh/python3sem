import matplotlib.pyplot as plt
import csv
import numpy as np


def sum_arr(k):
    sum_prep = np.zeros(len(prep_mark))
    sum_group = np.zeros(len(group_mark))
    for a in range(k):
        sum_prep += prep_mark[:, a]
        sum_group += group_mark[:, a]
    return (sum_prep, sum_group)


marks = []
group = []
prep = []

colors = ["#FF0000", "#FF7700", "#FFAB00", "#FFD500", "#FFFF00", "#DEFF00", "#9AFF00", "#1AFF00"]

with open("students.csv", 'r') as file:
    csv_read = csv.reader(file, delimiter=';')
    for student in csv_read:
        prep.append(int(student[0][-1]))
        group.append(int(student[1][-1]))
        marks.append(int(student[2]))

prep_mark = np.array([np.zeros(8) for i in range(7)])
group_mark = np.array([np.zeros(8) for i in range(6)])

for i in range(len(prep)):
    prep_mark[prep[i] - 1][marks[i] - 3] += 1
    group_mark[group[i] - 1][marks[i] - 3] += 1

fig, axs = plt.subplots(nrows=1, ncols=2)

axs[0].bar(["prep" + str(j + 1) for j in range(7)], prep_mark[:, 0], label=str(3), color=colors[0])
axs[1].bar([str(750 + j + 1) for j in range(6)], group_mark[:, 0], label=str(3), color=colors[0])

for i in range(1, 8):
    axs[0].bar(["prep" + str(j + 1) for j in range(7)], prep_mark[:, i], bottom=sum_arr(i)[0], label=str(i + 3),
               color=colors[i])
    axs[1].bar([str(750 + j + 1) for j in range(6)], group_mark[:, i], bottom=sum_arr(i)[1], label=str(i + 3),
               color=colors[i])

plt.legend(bbox_to_anchor=(1, 0.6))
figure = plt.gcf()
figure.set_size_inches(13, 6)
plt.savefig("marks.png")
