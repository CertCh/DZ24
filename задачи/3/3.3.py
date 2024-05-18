import csv

def process_large_csv(filename, column_name):
    total = 0
    count = 0

    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row[column_name])
            count += 1

    average = total / count if count != 0 else 0
    print(f"Среднее значение по столбцу '{column_name}': {average}")

process_large_csv("large_data.csv", "Temperature")
