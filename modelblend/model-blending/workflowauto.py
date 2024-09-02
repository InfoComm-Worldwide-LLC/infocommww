import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header row
        data = [row for row in csv_reader]
    return header, data

def process_data(data):
    processed_data = []
    for row in data:
        # Example: Add a new column with the sum of the first two columns
        new_row = row + [int(row[1]) + int(row[2])]
        processed_data.append(new_row)
    return processed_data

def write_csv(file_path, header, data):
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header + ['Sum'])  # Write the header with a new column
        csv_writer.writerows(data)

if __name__ == "__main__":
    input_file = 'input_data.csv'
    output_file = 'output_data.csv'

    header, data = read_csv(input_file)
    processed_data = process_data(data)
    write_csv(output_file, header, processed_data)

    print(f"Processed data saved to {output_file}")
