# # main.py
# import mypackage.module1
# import mypackage.module2
#
# mypackage.module1.greet('Pythonista')
# mypackage.module2.depart('Pythonista')

# main.py
from mypackage.module1 import greet
from mypackage.mysubpackage.module3 import people

for person in people:
    greet(person)
