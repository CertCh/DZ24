import csv

def create_csv():
    with open("data.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Имя", "Фамилия", "Возраст"])
        writer.writerow(["Иван", "Иванов", 30])
        writer.writerow(["Петр", "Петров", 25])
        writer.writerow(["Сергей", "Сергеев", 40])

create_csv()

def read_csv(filename):
    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))

read_csv("data.csv")
