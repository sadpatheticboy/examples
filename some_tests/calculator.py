# написать функцию calculator, которая принимает на вход строку, содержащую два целых числа и один знак арифметической
# операции + - / * и возвращает результат выполнения этой операции. Если числа не целые или нет знака операции то
# бросать исключение ValueError

def calculator(expression: str):
    allowed = '+-*/'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение не содержит нужные арифмитеские операции: {allowed}')

    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)

                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать два целых числа и одну арифмитическую операцию')


if __name__ == '__main__':
    print(calculator('2/1'))
