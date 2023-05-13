from unittest import TestCase, main
import doctest
from some_tests import divisor


def load_tests(loader, tests, ignore):  # Интеграция доктестов в работу юнит-тестов
    tests.addTests(doctest.DocTestSuite(divisor))
    return tests


class TestDivisor(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            divisor.divide(10, 0)


if __name__ == '__main__':
    main()