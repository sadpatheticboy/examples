import pytest

from something.calculator import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('abracadabra')
    assert 'Выражение не содержит нужные арифмитеские операции: +-*/' == error.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('2+2+2')
    assert 'Выражение должно содержать два целых числа и одну арифмитическую операцию' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
