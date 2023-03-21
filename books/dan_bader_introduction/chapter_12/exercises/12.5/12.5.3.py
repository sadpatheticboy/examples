with open('starhips.txt', mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        if line.startswith('D'):
            print(line, end='')
