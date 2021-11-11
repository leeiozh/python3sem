def gen_table(dataframe, sets, output_file):
    """
    фнукция техает табличку согласно sets по dataframe в output
    """
    caption = sets.get('caption')
    label = sets.get('label')
    center = sets.get('center')

    alignment = sets.get('alignment')
    order = sets.get("order").split(',')

    if len(order) != 0:
        with open(output_file, 'w') as output:
            output.write("\\begin{table}[h!]\n")
            if center:
                output.write("\\centering\n")  # есть ли параметр центровки таблицы
            if caption is not None:
                output.write("\\caption{" + caption + "}\n")  # есть ли название у таблицы
            output.write("\\begin{tabular}{")

            # параметры выравнивания внутри столбцов
            if len(alignment) == 1:
                for i in range(len(dataframe.columns)):
                    output.write("|" + alignment)
                output.write("|}\n")
            else:
                output.write(alignment + '}\n')
            output.write("\\hline\n")

            # заполнение таблицы
            for name in order:
                output.write(name)
                for num in dataframe[name].to_numpy():
                    output.write(' & ' + str(num))
                output.write("\\" + "\\ " + "\\hline\n")

            output.write("\\end{tabular}\n")
            if label is not None:
                output.write("\\label{" + label + '}\n')  # есть ли ярлык у таблицы
            output.write("\\end{table}\n")
