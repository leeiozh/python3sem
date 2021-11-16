import pandas as pd
import matplotlib.pyplot as plt

figure = plt.gcf()
figure.set_size_inches(12, 6)
colors = ["#FF0000", "#FF7700", "#FFAB00", "#FFD500", "#FFFF00", "#DEFF00", "#9AFF00", "#1AFF00"]

ejudge = pd.read_html("results_ejudge.html")[0]
groups = pd.read_excel("students_info.xlsx")

data = pd.merge(groups, ejudge, on='User')

res_fac = data.groupby('group_faculty')['Solved'].mean()
res_out = data.groupby('group_out')['Solved'].mean()

ax_0 = res_fac.plot(kind='bar', color=colors)
ax_0.set_title("group_in")
plt.savefig("ep3_group_in.png")
plt.clf()

ax_1 = res_out.plot(kind='bar', color=colors)
ax_1.set_title("group_in")
plt.savefig("ep3_group_out.png")
plt.clf()

print("Groups_in with best students....")
for i in data[(data['H'] > 0) | (data['G'] > 0)]['group_faculty']:
    print(i, end=' ')

print("\nGroups_out with best students....")

for i in data[(data['H'] > 0) | (data['G'] > 0)]['group_out']:
    print(i, end=' ')
