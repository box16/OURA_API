import unittest
from modules.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_create_average_list_1(self):
        calculator = Calculator()
        _input = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        _output = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertListEqual(calculator.create_average_list(_input), _output)

    def test_create_average_list_2(self):
        calculator = Calculator()
        _input = [[1, 2, 3, 4, 5], [1, 2, 3]]
        _output = [1.0, 2.0, 3.0, 2.0, 2.5]
        self.assertListEqual(calculator.create_average_list(_input), _output)

    def test_m_moving_average_odd(self):
        calculator = Calculator()
        _input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        _output = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
        self.assertListEqual(calculator.m_moving_average(_input, 3), _output)

    def test_m_moving_average_even(self):
        calculator = Calculator()
        _input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        _output = [3.0, 4.0, 5.0, 6.0, 7.0]
        self.assertListEqual(calculator.m_moving_average(_input, 4), _output)

    def test_create_combination_list_1(self):
        calculator = Calculator()
        _input = ["apple", "orange", "grape", "banana"]
        _output = [["apple", "orange"], ["apple", "grape"], ["apple", "banana"],
                   ["orange", "grape"], ["orange", "banana"],
                   ["grape", "banana"]]
        self.assertListEqual(
            calculator.create_combination_list(
                _input, 2), _output)

    def test_create_combination_list_2(self):
        calculator = Calculator()
        _input = ["apple", "orange", "grape", "banana"]
        _output = [["apple", "orange", "grape"], ["apple", "grape", "banana"],
                   ["orange", "grape", "banana"]]
        self.assertListEqual(
            calculator.create_combination_list(
                _input, 3), _output)


if __name__ == '__main__':
    unittest.main()
