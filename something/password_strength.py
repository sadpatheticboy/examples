# Написать функцию проверки "силы" пароля, возвращает всегда строку
#  - если пароль короче 8 символов то вернуть Тоо Weak
#  - если пароль содержит только цифры, только строчные, только заглавные то вернуть Weak
#  - если пароль содержит символы любых 2 наборов вернуть Good
#  - если пароль содержит символы любых 3 наборов, вернуть Very Good
import string


def password_strngth(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'

    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue

    if count == 3:
        return 'Very Good'

    return 'Weak' if count == 1 else 'Good'


if __name__ == '__main__':
    assert password_strngth('') == 'Too Weak'
    assert password_strngth('1234567') == 'Too Weak'
    assert password_strngth('abcdefg') == 'Too Weak'
    assert password_strngth('ABCDEFG') == 'Too Weak'
    assert password_strngth('1aA') == 'Too Weak'

    assert password_strngth('12345678') == 'Weak'
    assert password_strngth('1234567890') == 'Weak'
    assert password_strngth('abcdefgh') == 'Weak'
    assert password_strngth('ABCDEFGH') == 'Weak'
    assert password_strngth('ABCDEFGHJK') == 'Weak'

    assert password_strngth('1234abcd') == 'Good'
    assert password_strngth('1234ABCD') == 'Good'
    assert password_strngth('1234abcdef') == 'Good'
    assert password_strngth('abcdEABCDE') == 'Good'

    assert password_strngth('123abcABC') == 'Very Good'
    assert password_strngth('1234567aC') == 'Very Good'
    assert password_strngth('1abcdefgH') == 'Very Good'
    assert password_strngth('1aBCDEFGH') == 'Very Good'
