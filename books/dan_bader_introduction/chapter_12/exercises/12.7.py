import csv

with open('scores.txt', mode='r', encoding='utf-8', newline='') as file:
    text = csv.DictReader(file)
    scores = [row for row in text]

high_scores = {}
for item in scores:
    name = item["name"]
    score = int(item["score"])
    if name not in high_scores:
        high_scores[name] = score
    else:
        if score > high_scores[name]:
            high_scores[name] = score

with open('high_scores.txt', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "high_score"])
    writer.writeheader()
    for name in high_scores:
        row_dict = {"name": name, "high_score": high_scores[name]}
        writer.writerow(row_dict)
