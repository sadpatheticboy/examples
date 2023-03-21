word = ['Discovery\n', 'Enterprise\n', 'Defiant\n', 'Voyager\n']

with open('starhips.txt', mode='w', encoding='utf-8') as file:
    file.writelines(word)
