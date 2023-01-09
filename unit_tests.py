import unittest
from complex_numbers import ComplexNumber


class ComplexNumberTestCase(unittest.TestCase):
    """
    Юнит-тесты для класса ComplexNumber.
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

        cn_1 = ComplexNumber(-7)
        self.assertEqual(cn_1.re_z, -7)
        self.assertEqual(cn_1.im_z, 0)

    def test_get_pair_form(self):

        cn_1 = ComplexNumber()
        self.assertEqual(cn_1.get_pair_form(), (0, 0))

        cn_1 = ComplexNumber(6, -10)
        self.assertEqual(cn_1.get_pair_form(), (6, -10))

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
        self.assertEqual(cn_result.get_pair_form(), (1, -2))

        cn_list: list[ComplexNumber] = []
        for i in range(10):
            cn_list.append(ComplexNumber(5, -3))
        cn_result = ComplexNumber.sum(*cn_list)
        self.assertEqual(cn_result.get_pair_form(), (50, -30))

    def test_mul(self):

        cn_1 = ComplexNumber(4, 2)
        cn_2 = ComplexNumber(-10, -4)
        num_1 = (5, 2)
        self.assertRaises(Exception, ComplexNumber.sum, cn_1, cn_2, num_1)
        self.assertRaises(Exception, ComplexNumber.is_equal, cn_1, num_1, cn_2)

        cn_1 = ComplexNumber()
        cn_2 = ComplexNumber(10, -6)
        cn_result = ComplexNumber.mul(cn_1, cn_2)
        self.assertEqual(cn_result.get_pair_form(), (0, 0))

        cn_1 = ComplexNumber(5, -2)
        cn_2 = ComplexNumber(10, -6)
        cn_3 = ComplexNumber(6, 1)
        cn_4 = ComplexNumber()
        cn_result = ComplexNumber.mul(cn_1, cn_2, cn_3, cn_4)
        self.assertEqual(cn_result.get_pair_form(), (0, 0))

        cn_1 = ComplexNumber(2, 3)
        cn_2 = ComplexNumber(-3, 2)
        cn_3 = ComplexNumber(1, -1)
        cn_4 = ComplexNumber(2, 2)
        cn_result = ComplexNumber.mul(cn_1, cn_2, cn_3, cn_4)
        self.assertEqual(cn_result.get_pair_form(), (-48, -20))

    def test_get_opposite_by_sum(self):

        cp_1 = ComplexNumber()
        cp_result = cp_1.get_opposite_by_sum()
        self.assertEqual(cp_result.get_pair_form(), (0, 0))

        cp_1 = ComplexNumber(4, -3)
        cp_result = cp_1.get_opposite_by_sum()
        self.assertEqual(cp_result.get_pair_form(), (-4, 3))

        cp_1 = ComplexNumber(5, -20)
        cp_2 = cp_1.get_opposite_by_sum()
        cp_result = ComplexNumber.sum(cp_1, cp_2)
        self.assertEqual(cp_result.get_pair_form(), (0, 0))

    def test_get_opposite_by_mul(self):

        cp_1 = ComplexNumber(5, -13)
        cp_2 = cp_1.get_opposite_by_mul()
        cp_result = ComplexNumber.mul(cp_1, cp_2)
        self.assertEqual(cp_result.get_pair_form(), (1, 0))

    def test_get_conjugate(self):

        cn_1 = ComplexNumber(7, -3)
        cn_2 = cn_1.get_conjugate()
        cn_result = ComplexNumber.mul(cn_1, cn_2)
        answer = (cn_1.re_z ** 2) + (cn_1.im_z ** 2)
        self.assertEqual(cn_result.get_pair_form(), (answer, 0))

        cn_1 = ComplexNumber(5, 20)
        cn_2 = cn_1.get_conjugate()
        cn_3 = cn_2.get_conjugate()
        self.assertEqual(cn_1.get_pair_form() == cn_3.get_pair_form(), True)

        cn_1 = ComplexNumber(-11, 5)
        cn_2 = ComplexNumber(-4, -7)
        cn_1_2_sum = ComplexNumber.sum(cn_1, cn_2)
        cn_1_conj = cn_1.get_conjugate()
        cn_2_conj = cn_2.get_conjugate()
        self.assertEqual(
            cn_1_2_sum.get_conjugate().get_pair_form() == ComplexNumber.sum(cn_1_conj, cn_2_conj).get_pair_form(),
            True
        )

        cn_1 = ComplexNumber(4, -20)
        cn_2 = ComplexNumber(9, 6)
        cn_1_2_mul = ComplexNumber.mul(cn_1, cn_2)
        cn_1_conj = cn_1.get_conjugate()
        cn_2_conj = cn_2.get_conjugate()
        self.assertEqual(
            cn_1_2_mul.get_conjugate().get_pair_form() == ComplexNumber.mul(cn_1_conj, cn_2_conj).get_pair_form(),
            True
        )

    def test_div(self):

        cn_1 = ComplexNumber(7, -3)
        num_1 = (6, 8)
        self.assertRaises(Exception, ComplexNumber.div, cn_1, num_1)
        self.assertRaises(Exception, ComplexNumber.div, num_1, cn_1)

        cn_1 = ComplexNumber(6, -3)
        cn_2 = ComplexNumber()
        self.assertRaises(Exception, ComplexNumber.div, cn_1, cn_2)

        cn_1 = ComplexNumber(-1, 3)
        cn_2 = ComplexNumber(1, 2)
        cn_result = ComplexNumber.div(cn_1, cn_2)
        self.assertEqual(cn_result.get_pair_form(), (1, 1))

        cn_1 = ComplexNumber(13, 1)
        cn_2 = ComplexNumber(7, -6)
        cn_result = ComplexNumber.div(cn_1, cn_2)
        self.assertEqual(cn_result.get_pair_form(), (1, 1))



