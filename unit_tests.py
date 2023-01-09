import unittest
from complex_numbers import ComplexNumber


class ComplexNumberTestCase(unittest.TestCase):
    """
    Тесты для класса ComplexNumber.
    """

    def test_init(self):

        self.assertRaises(Exception, ComplexNumber, 6, "1")
        self.assertRaises(Exception, ComplexNumber, "1", -4)

        cn_1 = ComplexNumber()
        self.assertEqual(cn_1.re_z, 0)
        self.assertEqual(cn_1.im_z, 0)

        cn_1 = ComplexNumber(1, -5)
        self.assertEqual(cn_1.re_z, 1)
        self.assertEqual(cn_1.im_z, -5)

        cn_1 = ComplexNumber(-7, 2)
        self.assertEqual(cn_1.re_z, -7)
        self.assertEqual(cn_1.im_z, 2)

        cn_1 = ComplexNumber(6, -10)
        self.assertEqual(cn_1.pair_form, (6, -10))

    def test_is_complex_number(self):

        cn_list: list[ComplexNumber] = [ComplexNumber(1, 1) for i in range(10)]
        self.assertEqual(ComplexNumber.is_complex_number(*cn_list), True)

        num_list: list = [ComplexNumber(-1, -2) for i in range(10)]
        num_list.append(5)
        self.assertEqual(ComplexNumber.is_complex_number(*num_list), False)

    def test_is_equal(self):

        cn_1 = ComplexNumber(4, -8)
        cn_2 = ComplexNumber(4, -8)
        num_1 = (1, 7)
        self.assertRaises(Exception, ComplexNumber.is_equal, cn_1, cn_2, num_1)
        self.assertRaises(Exception, ComplexNumber.is_equal, cn_1, num_1, cn_2)

        cn_1 = ComplexNumber(4, -8)
        cn_2 = ComplexNumber(4, -8)
        self.assertEqual(ComplexNumber.is_equal(cn_1, cn_2), True)

        cn_1 = ComplexNumber(7, -3)
        cn_2 = ComplexNumber(7, 3)
        self.assertEqual(ComplexNumber.is_equal(cn_1, cn_2), False)

        cn_list: list[ComplexNumber] = []
        for i in range(10):
            cn_list.append(ComplexNumber(-6, -11))
        self.assertEqual(ComplexNumber.is_equal(*cn_list), True)

        cn_list: list[ComplexNumber] = []
        for i in range(5):
            cn_list.append(ComplexNumber(-7, 20))
        cn_list.append(ComplexNumber(7, 20))
        for i in range(5):
            cn_list.append(ComplexNumber(-7, 20))
        self.assertEqual(ComplexNumber.is_equal(*cn_list), False)

    def test_sum(self):

        cn_1 = ComplexNumber(3, 5)
        cn_2 = ComplexNumber(7, -2)
        num_1 = (6, 5)
        self.assertRaises(Exception, ComplexNumber.sum, cn_1, cn_2, num_1)
        self.assertRaises(Exception, ComplexNumber.is_equal, cn_1, num_1, cn_2)

        cn_1 = ComplexNumber(-6, -3)
        cn_2 = ComplexNumber(7, 1)
        cn_result = ComplexNumber.sum(cn_1, cn_2)
        self.assertEqual(cn_result.pair_form, (1, -2))

        cn_list: list[ComplexNumber] = []
        for i in range(10):
            cn_list.append(ComplexNumber(5, -3))
        cn_result = ComplexNumber.sum(*cn_list)
        self.assertEqual(cn_result.pair_form, (50, -30))


