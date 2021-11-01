import unittest, pytest
from somecode import Money, AnotherMoney


# Тесты, которые конечно же в другом коде я не пишу(
class MyTestCase(unittest.TestCase):

    money1 = Money('USD', 100)
    money2 = Money('EUR', 50)
    money3 = Money('USD', 30)
    money4 = Money('USD', 100)
    money5 = AnotherMoney('UAH', 1000)

    def test_init(self):
        self.assertEqual(self.money1.currency, 'USD', 'Маркировки не совпадают!!!')
        self.assertEqual(self.money3.amount, 30, 'Значения установленны не верно!!!')
        with self.assertRaises(ValueError, msg='Нельзя установить отрицательную валюту!!!'):
            Money.__init__(Money, 'USD', -1)

    def test_add(self):
        self.assertTrue(self.money4 + self.money3 == Money('USD', 130), 'Неправильный работает сложение!!!')

    def test_sub(self):
        self.assertTrue(self.money1 - self.money3 == Money('USD', 70), 'Проблемы с вычетанием!!!')
        with self.assertRaises(ValueError, msg='Ты должен, наверное?'):
            Money.__sub__(self.money3, self.money1)

    @unittest.skip('Скипаем')
    def test_str(self):
        self.assertTrue(str(self.money1) == 'USD, 100', 'Неправильный вывод на экран!!!')
        self.assertTrue(str(self.money2) == 'EUR, 50', 'Неправильный вывод на экран!!!')

    @unittest.skipIf(pytest.__version__ < '1.0',
                     'Скипаем')
    def test_eq(self):
        self.assertTrue(self.money1 == self.money4,
                        'Данные две валюты равны, а в результате тестирования, они оказались неравными!!!')
        self.assertFalse(self.money1 == self.money2,
                         'Данные две валюты неравны, а в результате тестирования, они оказались равными!!!')
        self.assertNotEqual(self.money1, self.money2,
                            'Данные две валюты неравны, а в результате тестирования, они оказались равными!!!')

    def test_types(self):
        self.assertIsInstance(self.money1, Money, 'Типы одинаковые, но оказались разными!!!')
        self.assertNotIsInstance(self.money1, AnotherMoney, 'Типы разные, но оказались одинаковыми!!!')


if __name__ == '__main__':
    unittest.main()
