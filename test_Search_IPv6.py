import unittest
from Search_IPv6 import CheckIPv6


class TestSearchIPv6(unittest.TestCase):
    """
    TestSearchIPv6
    Класс для проверки методов класса SearchIPv6
    """

    def setUp(self):  # Конфигурация тестов
        """Setup данных"""
        self.search = CheckIPv6()
        self.data = ("0:0:0:0:0:0:0:0 AB12:BC5:0:99:67:FF0:F:BCA bb55:BC5:120:99:0:FAB:f:BCaF 0:0:0:0:0:0:0 Z:BC5:0:99:"
                     "67:FF0:F:BCA 1:1:1:11111:1:1:1:1")
        self.correct_data = ["0:0:0:0:0:0:0:0", "AB12:BC5:0:99:67:FF0:F:BCA", "bb55:BC5:120:99:0:FAB:f:BCaF"]

    def test_check_string(self):  # Проверка метода поиска в строке (check_string)
        """Тест функции проверки строки на валидных данных"""

        self.assertEqual(self.search.check_string(mystring=self.data), self.correct_data)

    def test_check_file(self):  # Проверка метода поиска в файле (check_file)
        """Тест функции проверки строки на тестовом файле"""
        self.assertEqual(self.search.check_file(), ['54:12:1:534:98:434:54:12', '11Ff:12a:1B:534:98C:434:54:12'])

    def test_check_website(self):  # Проверка метода поиска на сайте (check_website)
        """Тест функции проверки сайта на тестовом html-коде"""

        self.assertEqual(self.search.check_website(),
                         ['2001:DB8:0:0:0:0:0:1', '2001:0db8:2023:0910:60e1:76bd:601e:fa2f',
                          '2001:0db8:2023:0910:36e1:7563:52e3:9043', '2001:0db8:2023:0910:baa2:45c8:8915:6d10',
                          '2001:0db8:2023:0910:baa2:45c8:8915:6d10', '2001:0db8:2023:0910:60e1:76bd:601e:fa2f',
                          '2001:0db8:2023:0910:36e1:7563:52e3:9043', '2001:DB8:0:0:0:0:0:1',
                          '2001:0db8:2023:0910:60e1:76bd:601e:fa2f', '2001:0db8:2023:0910:36e1:7563:52e3:9043',
                          '2001:0db8:2023:0910:baa2:45c8:8915:6d10', '2001:0db8:2023:0910:baa2:45c8:8915:6d10',
                          '2001:0db8:2023:0910:60e1:76bd:601e:fa2f', '2001:0db8:2023:0910:36e1:7563:52e3:9043'])


if __name__ == "__main__":
    unittest.main()
