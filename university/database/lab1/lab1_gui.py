import tkinter as tk

def find_elements():
    # получаем значения из полей ввода
    x_str = x_entry.get()
    c_str = c_entry.get()
    d_str = d_entry.get()

    # преобразуем значения в числа
    x = list(map(int, x_str.split()))
    c = int(c_str)
    d = int(d_str)

    # находим количество отрицательных элементов массива
    negative_count = sum(1 for i in x if i < 0)
    result_label.config(text=f'Количество отрицательных элементов: {negative_count}')

    # находим номера элементов, принадлежащих отрезку (C,D)
    indices = [i for i, v in enumerate(x) if c < v < d]
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f'Номера элементов от {c} до {d}: {indices}')
    result_text.config(state=tk.DISABLED)

# создаем графический интерфейс
root = tk.Tk()
root.title('Лабораторная работа №1, вариант 3')
root.geometry('400x300')

# создаем элементы интерфейса
x_label = tk.Label(root, text='Массив X')
x_entry = tk.Entry(root, width=50)
c_label = tk.Label(root, text='Нижняя граница')
c_entry = tk.Entry(root, width=10)
d_label = tk.Label(root, text='Верхняя граница')
d_entry = tk.Entry(root, width=10)
result_label = tk.Label(root, text='Результат:')
result_text = tk.Text(root, height=5, state=tk.DISABLED)
find_button = tk.Button(root, text='Найти', command=find_elements)

# размещаем элементы интерфейса на главном окне
x_label.pack()
x_entry.pack()
c_label.pack()
c_entry.pack()
d_label.pack()
d_entry.pack()
find_button.pack()
result_label.pack()
result_text.pack()

# запускаем главный цикл обработки событий
root.mainloop()
