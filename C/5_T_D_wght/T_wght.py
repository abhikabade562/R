import pandas as pd

class CellData:
    def __init__(self):
        self.count = 0
        self.tWeight = 0
        self.dWeight = 0

def read_csv_data(filename):
    try:
        df = pd.read_csv(filename)
        df = df.fillna(0)

        cell_data = {}
        column_total = {}
        row_total = {}

        for index, row in df.iterrows():
            row_name = str(row['Row'])
            col_name = str(row['Column'])
            count_value = int(row['Count'])

            if row_name not in cell_data:
                cell_data[row_name] = {}

            if col_name not in cell_data[row_name]:
                cell_data[row_name][col_name] = {'count': 0, 'tWeight': 0, 'dWeight': 0}

            cell_data[row_name][col_name]['count'] += count_value
            column_total[col_name] = column_total.get(col_name, 0) + count_value
            row_total[row_name] = row_total.get(row_name, 0) + count_value

        return cell_data, column_total, row_total

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None, None

def calculate_weights(cell_data, column_total, row_total):
    for row_name, row_data in cell_data.items():
        for col_name, cell in row_data.items():
            cell['tWeight'] = (cell['count'] / row_total[row_name]) * 100
            cell['dWeight'] = (cell['count'] / column_total[col_name]) * 100

def write_csv_result(filename, cell_data, column_total, row_total):
    with open(filename, 'w') as file:
        file.write("Column\\Row, Count, T-Weight, D-Weight, Count, T-Weight, D-Weight, Count, T-Weight, D-Weight\n")

        for row, row_total_value in row_total.items():
            file.write(f"{row},")

            for col, col_total_value in column_total.items():
                cell = cell_data[row][col]
                file.write(f"{cell['count']},")
                file.write(f"{cell['tWeight']:.2f}%,")
                file.write(f"{cell['dWeight']:.2f}%,")
            
            file.write(f"{row_total_value},100%, {row_total_value / list(row_total.values())[0] * 100:.2f}%\n")

        file.write("Total,")

        for col, col_total_value in column_total.items():
            file.write(f"{col_total_value},")
            file.write(f"{col_total_value / list(column_total.values())[0] * 100:.2f}%,100%,")

        file.write(f"{list(column_total.values())[0]},100%, 100%\n")

if __name__ == "__main__":
    input_filename = "Input_File.csv"
    output_filename = "Output_File.csv"

    cell_data, column_total, row_total = read_csv_data(input_filename)

    if cell_data is not None:
        calculate_weights(cell_data, column_total, row_total)
        write_csv_result(output_filename, cell_data, column_total, row_total)
        print("\nCheck 'Output_File.csv' for the result")
