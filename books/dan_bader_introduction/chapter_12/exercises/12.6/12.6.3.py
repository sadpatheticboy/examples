import csv

favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

with open('favorite_colors.txt', mode="w", encoding="utf-8", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "favorite_color"])
    writer.writeheader()
    writer.writerows(favorite_colors)
