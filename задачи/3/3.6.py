import os
import csv

def analyze_directory(directory):
    statistics = {
        "total_age": 0,
        "count": 0,
        "location_counts": {}
    }

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            with open(os.path.join(directory, filename), newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    age = int(row.get("Возраст", 0))
                    location = row.get("Местоположение", "Unknown")
                    statistics["total_age"] += age
                    statistics["count"] += 1
                    if location not in statistics["location_counts"]:
                        statistics["location_counts"][location] = 0
                    statistics["location_counts"][location] += 1
    
    average_age = statistics["total_age"] / statistics["count"] if statistics["count"] != 0 else 0
    print(f"Средний возраст: {average_age}")
    print("Распределение по местоположению:")
    for location, count in statistics["location_counts"].items():
        print(f"{location}: {count}")

analyze_directory("data")
