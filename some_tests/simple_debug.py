def get(value):
    if value > 0:
        return 'Pozitive'
    if value < 0:
        return 'Negative'


if __name__ == '__main__':
    value = int(input())
    print(get(value).upper())
