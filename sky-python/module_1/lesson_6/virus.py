virus_code = 'print("Я вирус")'

with open('write_file.py', 'a', encoding='utf-8') as file:
    file.write(f'{virus_code}\n')
