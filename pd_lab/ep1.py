import pandas as pd

df = pd.read_csv("transactions.csv", index_col='num')

df_ok = df[df['STATUS'] == 'OK']

print("Three big ok sum....\n", df_ok.loc[df_ok['SUM'].nlargest(3).index])
print()
print("Umbrella, Inc sum....\n", df_ok[df_ok['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum())