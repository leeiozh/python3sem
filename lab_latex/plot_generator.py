import matplotlib.pyplot as plt


def gen_plot(dataframe, sets, output_file):

    print(sets)

    x = dataframe[sets.get('x')].to_numpy()
    y = dataframe[sets.get('y')].to_numpy()
    color = sets.get('color')

    plt.plot(x, y, color=color)
    plt.savefig(output_file)

