import unittest
import IntegerDivision


class MyListTests(unittest.TestCase):

    def setUp(self):
        self.obj_1 = IntegerDivision.Division('625', '5')
        self.obj_2 = IntegerDivision.Division('42', '12')
        self.obj_3 = IntegerDivision.Division('0', '234')
        self.obj_4 = IntegerDivision.Division('16008', '12')
        self.obj_5 = IntegerDivision.Division('42014', '14')
        self.obj_6 = IntegerDivision.Division('12', '13')

    def test_normal(self):
        self.assertEqual(IntegerDivision.Division.division_in_column(self.obj_1), '_625|_5__5_ |125_12_10_ _25 _25_   0')

    def test_twoconsiderable_numbers(self):
        self.assertEqual(IntegerDivision.Division.division_in_column(self.obj_2), '_42 |_12__36_|3,5 _60 _60_   0')

    def test_divided_zero(self):
        self.assertEqual(IntegerDivision.Division.division_in_column(self.obj_3), ' 0 |_234__0_|0 0 ')

    def test_zeros_in_divided(self):
        self.assertEqual(IntegerDivision.Division.division_in_column(self.obj_4), '_16008|_12__12_  |1334 _40 _36_  _40  _36_   _48   _48_     0')

    def test_zeros_in_part(self):
        self.assertEqual(IntegerDivision.Division.division_in_column(self.obj_5), '_42014|_14__42_  |3001   _14   _14_     0')

    def test_remain(self):
        self.assertEqual(IntegerDivision.Division.division_in_column(self.obj_6), '_12|_13__0_|0,923076923_120_117_  _30  _26_   _40   _39_    _100     _91_      _90      _78_      _120      _117_        _30        _26_         _40         ...')


if __name__ == '__main__':
    unittest.main()