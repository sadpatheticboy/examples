from enum import Enum, auto


class Weekdays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


w = Weekdays(2)
print(w)

print(Weekdays.SUNDAY)
print(Weekdays.SUNDAY.value)

for day in Weekdays:
    print(day.name, day.value)


class Colors(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()


print(Colors.GREEN.value)
