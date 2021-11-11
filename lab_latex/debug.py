import table_generator
import data_reader

data_file = "my_data.csv"
set_file = "settings.txt"
output_file = "test0.txt"

table_generator.gen_table(data_reader.read_data(data_file), data_reader.read_set(set_file), output_file)
