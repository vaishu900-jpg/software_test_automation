import csv

with open("login_test_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
