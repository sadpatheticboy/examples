"""На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит
 натуральное число из отрезка [a;b] с максимальной суммой делителей"""

a, b = int(input()), int(input())
largest = 0
total = 0
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += j
        if count >= total:
            total = count
            largest = i
print(largest, total)
