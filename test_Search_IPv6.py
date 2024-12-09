import unittest
from Search_IPv6 import Check_IPv6


class TestCheckAll(unittest.TestCase):

    def setUp(self):
        """Setup данных"""
        self.search = Check_IPv6()
        self.data = "0:0:0:0:0:0:0:0 AB12:BC5:0:99:67:FF0:F:BCA bb55:BC5:120:99:0:FAB:f:BCaF 0:0:0:0:0:0:0 Z:BC5:0:99:67:FF0:F:BCA 1:1:1:11111:1:1:1:1"
        self.correct_data = ["0:0:0:0:0:0:0:0", "AB12:BC5:0:99:67:FF0:F:BCA", "bb55:BC5:120:99:0:FAB:f:BCaF"]

    def test_check_string(self):
        """Тест функции проверки строки на валидных данных"""

        self.assertEqual(self.search.check_string(string=self.data), self.correct_data)


if __name__ == "__main__":
    unittest.main()