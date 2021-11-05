from params_test import FILENAME

# Код для тестирования :)
# Тестовый класс
class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        if amount < 0:
            raise ValueError('Значение не может быть отрицательным!')
        else:
            self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money) and (self.currency == other.currency):
            return Money(self.currency, self.amount + other.amount)
        else:
            raise ValueError

    def __sub__(self, other):
        if (type(other) is Money) and (self.currency == other.currency):
            return Money(self.currency, self.amount - other.amount)
        else:
            raise ValueError

    def __eq__(self, other):
        return self.amount == other.amount

    def __str__(self):
        return '{0}, {1}'.format(self.currency, self.amount)

    def __repr__(self):
        return 'Currency: {0}\nAmount: {1}'.format(self.currency, self.amount)


# Тестовый наследник
class AnotherMoney(Money):
    pass


# Тестовая функция для работы с файлами
def file_func(filename, *args, **kwargs):
    for i in args:
        with open(filename, 'a', encoding='utf-8') as file:
            file.writelines(f'Arg: {i}\n')
    for i, j in kwargs:
        with open(filename, 'a', encoding='utf-8') as file:
            file.writelines(f'Kwarg: {i}: {j}\n')

    """with open(filename, 'r', encoding='utf-8') as file:
        a = file.read()
        print(a)"""


def main():
    file_func(FILENAME)


if __name__ == '__main__':
    main()