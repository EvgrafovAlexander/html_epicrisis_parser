import unittest
from scripts import table_finder


class TestTableFinder(unittest.TestCase):
    def test_is_unit_matched_1(self):
        value = '0.23(сек.)'
        units = ['(сек.)']
        result = table_finder.is_unit_matched(value, units)
        self.assertEqual(True, result)

    def test_is_unit_matched_2(self):
        value = '0.23 сек'
        units = ['(сек.)', 'сек']
        result = table_finder.is_unit_matched(value, units)
        self.assertEqual(True, result)

    def test_is_unit_matched_4(self):
        value = '0.23'
        units = ['']
        result = table_finder.is_unit_matched(value, units)
        self.assertEqual(True, result)

    def test_is_unit_matched_3(self):
        value = '0.23 сек'
        units = ['(г/л)']
        result = table_finder.is_unit_matched(value, units)
        self.assertEqual(False, result)

    def test_value_parser_1(self):
        value = '0.23(сек.)'
        value_type = 'float'
        units = ['(сек.)']
        result = table_finder.value_parser_float(value, value_type, units, 'column')
        self.assertEqual(0.23, result)

    def test_value_parser_2(self):
        value = '23(сек.)'
        value_type = 'float'
        units = ['(сек.)']
        result = table_finder.value_parser_float(value, value_type, units, 'column')
        self.assertEqual(23, result)

    def test_value_parser_3(self):
        value = '23  (сек.)'
        value_type = 'float'
        units = ['(сек.)']
        result = table_finder.value_parser_float(value, value_type, units, 'column')
        self.assertEqual(23, result)

    def test_value_parser_4(self):
        value = '20.23  '
        value_type = 'float'
        units = ['']
        result = table_finder.value_parser_float(value, value_type, units, 'column')
        self.assertEqual(20.23, result)


if __name__ == '__main__':
    unittest.main()
