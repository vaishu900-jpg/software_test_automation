import csv

with open("employee_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
