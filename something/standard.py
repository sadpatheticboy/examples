# a_list = [1, 0, True]
# b_list = []
#
# if any(a_list):
#     print(list(filter(None, a_list)))
#     print([e for e in a_list if e])


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat({self.name=}, {self.age=})'


if __name__ == '__main__':
    cats = [Cat('Tom', 3), Cat('Angela', 4), Cat('Bob', 5)]
    # print(max(cats, key=lambda cat: cat.name))

    # print(all(a_list))  # False
    # print(any(a_list))  # True
    #
    # print(all(b_list))  # True
    # print(any(b_list))  # False

    # for line in iter(input, 'end'):
    #     print(line.upper())
    ints = [int(e) for e in iter(input, '')]
    print(ints)
