"""https://stepik.org/lesson/740203/step/12?unit=741843"""

import csv
from datetime import datetime
from collections import namedtuple
Guests = namedtuple('Guests', ['surname', 'name', 'date', 'time'])
plans = []
with open('meetings.csv', 'r', encoding='utf-8', newline='') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    for row in reader:
        plans.append(Guests._make(row.values()))
print(*list(map(lambda a: f'{a.surname} {a.name}', sorted(plans, key=lambda x: datetime.strptime(x.date+x.time, '%d.%m.%Y%H:%M')))), sep='\n')
