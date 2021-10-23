import pandas as pd
import matplotlib.pyplot as plt

ejudge = pd.read_html("results_ejudge.html")[0]
groups = pd.read_excel("students_info.xlsx")

data = pd.merge(groups, ejudge, on='User')

group_faculty = groups['group_faculty'].unique()
group_out = groups['group_out'].unique()

res_fac = [data[data['group_faculty'] == i]['Solved'].mean() for i in group_faculty]
res_out = [data[data['group_out'] == i]['Solved'].mean() for i in group_out]

fig, axs = plt.subplots(nrows=1, ncols=2)
colors = ["#FF0000", "#FF7700", "#FFAB00", "#FFD500", "#FFFF00", "#DEFF00", "#9AFF00", "#1AFF00"]

axs[0].bar([str(i) for i in group_faculty], res_fac, color=colors)
axs[0].set_title("group_in")
axs[1].bar([str(i) for i in group_out], res_out, color=colors)
axs[1].set_title("group_out")

figure = plt.gcf()
figure.set_size_inches(12, 6)
plt.savefig("number_of_solved_tasks.png")

print("Groups_in with best students....")
for i in data[(data['H'] > 0) | (data['G'] > 0)]['group_faculty']:
    print(i, end=' ')

print("\nGroups_out with best students....")

for i in data[(data['H'] > 0) | (data['G'] > 0)]['group_out']:
    print(i, end=' ')
