import matplotlib.pyplot as plt
import csv
import numpy as np


def sum_arr(k):
    sum_prep = np.zeros(len(prep_m))
    sum_group = np.zeros(len(group_m))
    for a in range(k):
        sum_prep += np.array([mark[1][a] for mark in prep_m.items()])
        sum_group += np.array([mark[1][a] for mark in group_m.items()])
    return sum_prep, sum_group


howmanymarks = 10  # скольки балльная шкала (включая ноль) используется
colors = ["#A200FF", "#FF00FF", "#FF0091", "#FF0000", "#FF7700", "#FFAB00", "#FFD500", "#FFFF00", "#DEFF00", "#9AFF00",
          "#1AFF00"]
marks = []
group = []
prep = []

with open("students.csv", 'r') as file:
    csv_read = csv.reader(file, delimiter=';')
    for student in csv_read:
        prep.append(student[0])
        group.append(student[1])
        marks.append(int(student[2]))

prep_m = {prep: np.zeros(howmanymarks + 1) for prep in list(set(sorted(prep)))}
group_m = {group: np.zeros(howmanymarks + 1) for group in list(set(sorted(group)))}

for i in range(len(prep)):
    prep_m.get(prep[i])[marks[i]] += 1
    group_m.get(group[i])[marks[i]] += 1

fig, axs = plt.subplots(nrows=1, ncols=2)

axs[0].bar(prep_m.keys(), [mark[1][0] for mark in prep_m.items()], label=str(0), color=colors[0])
axs[1].bar(group_m.keys(), [mark[1][0] for mark in group_m.items()], label=str(0), color=colors[0])

for i in range(1, howmanymarks + 1):
    axs[0].bar(prep_m.keys(), [mark[1][i] for mark in prep_m.items()], bottom=sum_arr(i)[0], label=str(i),
               color=colors[i % len(colors)])
    axs[1].bar(group_m.keys(), [mark[1][i] for mark in group_m.items()], bottom=sum_arr(i)[1], label=str(i),
               color=colors[i % len(colors)])

plt.legend(bbox_to_anchor=(1, 0.6))
figure = plt.gcf()
figure.set_size_inches(13, 6)
plt.savefig("marks.png")
