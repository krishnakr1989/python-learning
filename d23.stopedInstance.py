import csv

with open("d23.data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["environment"] == "prod" and row["status"] == "stopped":
            print(row["instance"])