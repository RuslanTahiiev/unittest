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



