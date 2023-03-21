lines_of_text = [
    "Hello from Line l\n",
    "Hello from Line 2\n",
    "Hello from Line 3\n"]

with open('test.txt', mode="w", encoding="utf-8") as file:
    file.writelines(lines_of_text)

with open('new_test.txt', mode='w', encoding='utf-8') as file:
    file.write('Hello!')