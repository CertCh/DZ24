import csv

def sum_column(file_path, column_name):
    total = 0
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total += float(row[column_name])
    return total

file_path = 'data.csv'
column_name = 'Amount'
print(sum_column(file_path, column_name))
