import csv

def average_of_columns(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        columns = []
        for row in reader:
            if not columns:
                columns = [[] for _ in row]
            for i, value in enumerate(row):
                columns[i].append(float(value))
        
        averages = [sum(col) / len(col) for col in columns]
        for i, avg in enumerate(averages):
            print(f"Среднее арифметическое чисел в колонке {i + 1}: {avg}")

filename = input("Введите имя файла CSV: ")
average_of_columns(filename)
