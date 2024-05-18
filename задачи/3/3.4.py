import csv

def merge_csv_files(filenames, output_filename):
    combined_data = []
    headers = set()

    for filename in filenames:
        with open(filename, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            headers.update(reader.fieldnames)
            for row in reader:
                combined_data.append(row)
    
    headers = list(headers)

    with open(output_filename, "w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in combined_data:
            writer.writerow(row)

merge_csv_files(["data1.csv", "data2.csv", "data3.csv"], "combined_data.csv")
