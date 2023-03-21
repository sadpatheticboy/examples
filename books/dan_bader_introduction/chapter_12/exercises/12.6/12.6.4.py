import csv

result = []

with open('favorite_colors.txt', mode='r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        result.append(row)

print(result)
