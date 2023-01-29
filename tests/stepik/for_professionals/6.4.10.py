"""https://stepik.org/lesson/740203/step/10?unit=741843"""

from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)
    for i in obj:
        print(f'{Animal._fields[0]}: {i[0]}')
        print(f'{Animal._fields[1]}: {i[1]}')
        print(f'{Animal._fields[2]}: {i[2]}')
        print(f'{Animal._fields[3]}: {i[3]}')
        print()


