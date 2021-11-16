import pandas as pd
import matplotlib.pyplot as plt

figure = plt.gcf()
figure.set_size_inches(12, 6)
colors = ["red", "orange", "yellow"]
df = pd.read_csv("flights.csv", index_col='num')
df_cargo = df.groupby('CARGO')

ax_0 = df_cargo["PRICE"].sum().plot(kind='barh', color=colors)
ax_0.set_title("sums")
plt.savefig("ep2_sum.png")
plt.clf()

ax_1 = df_cargo["WEIGHT"].sum().plot(kind='barh', color=colors)
ax_1.set_title("weights")
plt.savefig("ep2_weight.png")
plt.clf()

ax_2 = df_cargo["WEIGHT"].count().plot(kind='barh', color=colors)
ax_2.set_title("flights")
plt.savefig("ep2_flights.png")
plt.clf()