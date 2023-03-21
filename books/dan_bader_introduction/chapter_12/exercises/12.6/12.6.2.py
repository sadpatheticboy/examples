import csv

result = []
with open('numbers.txt', mode='r', encoding='utf-8', newline='') as file:
    writer = csv.reader(file)
    for row in writer:
        result.append([int(i) for i in row])

print(result)
