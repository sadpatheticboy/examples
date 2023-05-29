class MyClass:
    def __enter__(self):
        print('Метод enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Метод exit')


my_o = MyClass()

with my_o:  # Переход в метод __enter__()
    print('Context')  # Исполнение контекста
    # raise ZeroDivisionError  # Также вызов метода __exit__()
    c = 1

print('Конец')  # Контекст закончился, вызов метода __exit__() кастомного класса MyClass()
