from collections.abc import Iterator

print('[ITERATOR]')


class StringByLetter:
    def __init__(self, string):
        self.string = string
        self.len_str = len(string)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.len_str:
            letter = self.string[self.position]
            self.position += 1
            return letter.upper()
        raise StopIteration


for letter in StringByLetter('Hello!'):
    print(letter)

print('\n[GENERATOR]')


def string_by_letter(string):  # Generator
    for letter in string:
        yield letter.upper()


for letter in string_by_letter('Hello!'):
    print(letter)

gen = string_by_letter('Hello!')
print(f'\nГенератор - наследник итератора: isinstance(gen, Iterator) = {isinstance(gen, Iterator)}')
