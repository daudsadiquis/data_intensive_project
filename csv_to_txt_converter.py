import csv

# Read the CSV file with 'ISO-8859-1' encoding
with open("test_dataset.csv", "r", encoding='ISO-8859-1') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Write the content to a TXT file
    with open("test_dataset.txt", "w", encoding='utf-8') as txt_file:
        for row in csv_reader:
            txt_file.write(','.join(row) + '\n')
