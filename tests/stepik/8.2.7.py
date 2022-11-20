"""https://stepik.org/lesson/294080/step/7?thread=solutions&unit=275759"""

n = 50000
for i in range(1, n + 1):
    count = 0
    for x in range(1, int(i ** (1 / 3)) + 1):
        for y in range(x, int(i ** (1 / 3)) + 1):
            if x ** 3 + y ** 3 == i:
                count += 1
            elif x ** 3 + y ** 3 > i:
                break
    if count >= 2:
        print(i)
