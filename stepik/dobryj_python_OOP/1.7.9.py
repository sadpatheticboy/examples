""" Условие задачи - https://stepik.org/lesson/701978/step/9?unit=702079 """

from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        nums = number.split('-')
        if len(nums) != 4:
            return False
        for i in nums:
            if '0000' > i or i > '9999' or len(i) != 4 or i.isdigit() == False:
                return False
        return True

    @staticmethod
    def check_name(name):
        name = name.split()
        if len(name) != 2:
            return False
        for i in name:
            if not set(i) < set(CardCheck.CHARS_FOR_NAME) or i.upper() != i:
                return False
        return True

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

print(is_number)
print(is_name)