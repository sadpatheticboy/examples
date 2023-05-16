from useful.time_measure import time_measure

n = 1_000_000
l = list(range(n))


@time_measure
def for_loop():
    for i in l:
        i += 1


@time_measure
def enumerate_loop():
    for i, elem in enumerate(l):
        elem += 1


@time_measure
def compr_loop():
    [i + 1 for i in l]


@time_measure
def for_with_range():
    for i in range(len(l)):
        l[i] += 1


@time_measure
def while_loop():
    i = 0
    while i < len(l):
        l[i] += 1
        i += 1


for_loop()
enumerate_loop()
compr_loop()
for_with_range()
while_loop()

print('=' * 20)


@time_measure
def create_list_with_range():
    l = list(range(n))


@time_measure
def create_list_with_listcomps():
    l = [i for i in range(n)]


@time_measure
def create_list_with_genexp():
    l = (i for i in range(n))


create_list_with_range()
create_list_with_listcomps()
create_list_with_genexp()
