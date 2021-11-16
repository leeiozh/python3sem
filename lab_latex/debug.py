import table_generator
import plot_generator
import data_reader

data_file = "my_data.csv"
set_file_table = "settings_table.txt"
set_file_plot = "settings_plot.txt"
output_file = "test0.txt"
output_plot = "test0.png"

# table_generator.gen_table(data_reader.read_data(data_file), data_reader.read_set(set_file_table), output_file)
plot_generator.gen_plot(data_reader.read_data(data_file), data_reader.read_set(set_file_plot), output_plot)

