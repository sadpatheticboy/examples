guests_count = 0

with open('guests.txt', 'rt', encoding="utf-8") as file:
    for line in file:
        guests_count += 1
        print(line)

print(f"Количество гостей = {guests_count}")
