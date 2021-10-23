import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flights.csv", index_col='num')

companies = df['CARGO'].unique()
colors = ["red", "orange", "yellow"]

sums = [df[df['CARGO'] == i]['PRICE'].sum() for i in companies]
weights = [df[df['CARGO'] == i]['WEIGHT'].sum() for i in companies]
lens = [df[df['CARGO'] == i].shape[0] for i in companies]

fig, axs = plt.subplots(nrows=1, ncols=3)

axs[0].bar(companies, sums, color=colors)
axs[0].set_title("sums")
axs[1].bar(companies, weights, color=colors)
axs[1].set_title("weights")
axs[2].bar(companies, lens, color=colors)
axs[2].set_title("flights")

figure = plt.gcf()
figure.set_size_inches(18, 6)
plt.savefig("flightss.png")
