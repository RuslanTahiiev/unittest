import pytest
from somecode import Money, file_func
from params_test import FILENAME, money_list, file_list_generator

money1 = Money('USD', 100)
money2 = Money('USD', 30)
money3 = Money('USD', 100)


def test_eq():
    assert money1 == money3


def test_add():
    assert money1 + money2 == Money('USD', 130)


@pytest.mark.parametrize('value1, value2, currency, exp_res', money_list)
def test_sub(value1, value2, currency, exp_res):
    assert Money(currency, value1) - Money(currency, value2) == Money(currency, exp_res)


def test_error():
    with pytest.raises(ValueError):
        m = Money('EUR', -1)


@pytest.mark.parametrize('args', file_list_generator(101))
def test_file_func(args):
    test_lines = f'Arg: {args}\n'
    file_func(FILENAME, args)
    with open(FILENAME, 'r', encoding='utf-8') as file:
        assert test_lines == file.read()
