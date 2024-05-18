import csv
import statistics

def column_statistics(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {field: [] for field in reader.fieldnames}
        for row in reader:
            for field in row:
                try:
                    data[field].append(float(row[field]))
                except ValueError:
                    continue
    
    for field in data:
        if data[field]:
            print(f"Statistics for {field}:")
            print(f"  Mean: {statistics.mean(data[field])}")
            print(f"  Median: {statistics.median(data[field])}")
            print(f"  Standard Deviation: {statistics.stdev(data[field])}")

file_path = 'data.csv'
column_statistics(file_path)
