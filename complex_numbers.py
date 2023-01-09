import copy
import typing as tp


class ComplexNumber:
    """
    Класс для реализации комплексного числа и сопутствующих функций.
    """

    def __init__(self, re_z: tp.Union[int, float] = 0, im_z: tp.Union[int, float] = 0):
        """
        Инициализируем комплексное число при создании экземпляра класса.
        :param re_z: Вещественная часть числа.
        :param im_z: Мнимая часть числа.
        """

        # Проверяем, что введены числовые коэффициенты, и если это не так, то выбрасываем ошибку
        if not(isinstance(re_z, (int, float))) or not(isinstance(im_z, (int, float))):
            raise Exception("Введены нечисловые коэффициенты для комплексного числа")

        # Задаём вещественную и мнимую часть комплексного числа
        self.re_z = re_z
        self.im_z = im_z

    def get_pair_form(self) -> tuple[tp.Union[int, float], tp.Union[int, float]]:
        """
        Функция для получения комплексного числа в формате картежа из двух чисел.
        :return: Картеж из двух чисел - вещественной и мнимой части.
        """
        return self.re_z, self.im_z

    @staticmethod
    def is_equal(num_1: 'ComplexNumber', num_2: 'ComplexNumber', *nums: 'ComplexNumber') -> bool:
        """
        Функция для проверки на равенство нескольких комплексных чисел.
        :param num_1: Первое комплексное число.
        :param num_2: Второе комплексное число.
        :param nums: Дополнительные комплексные числа.
        :return: Результат сравнения. True - если все введённые числа равны, False - в противном случае.
        """

        # Если переданные объекты не являются комплексными числами, то выбрасываем ошибку
        if not(ComplexNumber.is_complex_number(num_1, num_2, *nums)):
            raise Exception("Функция ComplexNumber.is_equal() работает только с объектами класса ComplexNumber")

        # Берём первое введённое комплексное число как текущее
        current_num = num_1

        # Перебираем все оставшиеся числа
        for num in [num_2, *nums]:

            # Если текущее и итерируемое числа равны, то устанавливаем итерируемое число как текущее и повторяем цикл
            if (current_num.re_z == num.re_z) and (current_num.im_z == num.im_z):
                current_num = num
                continue
            # Иначе возвращаем False
            else:
                return False

        # Если все проверки прошли, то возвращаем True
        return True

    @staticmethod
    def sum(num_1: 'ComplexNumber', num_2: 'ComplexNumber', *nums: 'ComplexNumber') -> 'ComplexNumber':
        """
        Функция для сложения нескольких комплексных чисел.
        :param num_1: Первое комплексное число.
        :param num_2: Второе комплексное число.
        :param nums: Дополнительные комплексные числа.
        :return: Новое комплексное число, являющее результатом суммы переданных комплексных чисел.
        """

        # Если переданные объекты не являются комплексными числами, то выбрасываем ошибку
        if not(ComplexNumber.is_complex_number(num_1, num_2, *nums)):
            raise Exception("Функция ComplexNumber.sum() работает только с объектами класса ComplexNumber")

        # Создаём нулевое комплексное число
        num_sum = ComplexNumber()

        # Перебираем все переданные числа, складывая их вещественные и мнимые части с таковыми у созданного выше числа
        for num in [num_1, num_2, *nums]:
            num_sum.re_z += num.re_z
            num_sum.im_z += num.im_z

        # Возвращаем комплексное число с вещественной и мнимой частями, полученными в результате сложения
        return num_sum

    @staticmethod
    def is_complex_number(*nums) -> bool:
        """
        Функция, проверяющая, являются ли переданные объекты комплексными числами.
        :param nums: Объекты для проверки.
        :return: True - если переданные объекты являются комплексными числами, False - в противном случае.
        """

        # Перебираем все переданные объекты, и если они все относятся к классу ComplexNumber, то возвращаем True
        # Иначе возвращаем False
        for num in nums:
            if not(isinstance(num, ComplexNumber)):
                return False
        return True

    @staticmethod
    def mul(num_1: 'ComplexNumber', num_2: 'ComplexNumber', *nums: 'ComplexNumber') -> 'ComplexNumber':
        """
        Функция для перемножения нескольких комплексных чисел.
        :param num_1: Первое комплексное число.
        :param num_2: Второе комплексное число.
        :param nums: Дополнительные комплексные числа.
        :return: Комплексное число, являющееся результатом перемножения заданных комплексных чисел.
        """

        # Если переданные объекты не являются комплексными числами, то выбрасываем ошибку
        if not (ComplexNumber.is_complex_number(num_1, num_2, *nums)):
            raise Exception("Функция ComplexNumber.mul() работает только с объектами класса ComplexNumber")

        # За изначальное значение берём первое переданное число (копируем его)
        num_mul = copy.deepcopy(num_1)

        # Перебираем все оставшиеся комплексные числа и поочерёдно перемножаем их с изначальным
        for num in [num_2, *nums]:
            a = num_mul.re_z
            b = num_mul.im_z
            c = num.re_z
            d = num.im_z
            num_mul.re_z = (a * c) - (b * d)
            num_mul.im_z = (a * d) + (b * c)

        # Возвращаем комплексное число, являющееся произведением все переданных чисел
        return num_mul

    def get_opposite_by_sum(self) -> 'ComplexNumber':
        """
        Функция, возвращающая обратное комплексное число по сумме.
        :return: Обратное комплексное число по сумме.
        """
        return ComplexNumber(-self.re_z, -self.im_z)

    def get_opposite_by_mul(self) -> 'ComplexNumber':
        """
        Функция, возвращающая обратное комплексное число по произведению.
        :return: Обратное комплексное число по произведению.
        """

        # Находим обратное комплексное число по формуле и возвращаем его
        a = self.re_z
        b = self.im_z
        a_opposite = a / ((a ** 2) + (b ** 2))
        b_opposite = -b / ((a ** 2) + (b ** 2))
        return ComplexNumber(a_opposite, b_opposite)
        pass

    def get_conjugate(self) -> 'ComplexNumber':
        """
        Функция, возвращающая сопряжённое комплексное число.
        :return: Сопряжённое комплексное число.
        """
        return ComplexNumber(self.re_z, -self.im_z)

    @staticmethod
    def div(num_1: 'ComplexNumber', num_2: 'ComplexNumber') -> 'ComplexNumber':
        """
        Функция для деления одного комплексного числа на другое.
        :param num_1: Делимое (комплексное число).
        :param num_2: Делитель (комплексное число).
        :return: Результат деления (комплексное число).
        """

        # Если переданные объекты не являются комплексными числами, то выбрасываем ошибку
        if not (ComplexNumber.is_complex_number(num_1, num_2)):
            raise Exception("Функция ComplexNumber.div() работает только с объектами класса ComplexNumber")

        # Если делитель равен нулю, то выводим сообщение об ошибке
        if num_2.get_pair_form() == (0, 0):
            raise Exception("Функция ComplexNumber.div() на способно делить на ноль")

        # Преобразуем числитель и знаменатель получившийся дроби
        numerator = ComplexNumber.mul(num_1, num_2.get_conjugate())
        denominator = ComplexNumber.mul(num_2, num_2.get_conjugate())

        # Вытаскиваем из знаменателя вещественное число (т.к. мнимая часть равно нулю)
        denominator = denominator.re_z

        # Преобразуем знаменатель в комплексное число вида (1/re_z, 0)
        denominator = ComplexNumber(1 / denominator, 0)

        # Умножаем числитель на преобразованный знаменатель
        num_div = ComplexNumber.mul(numerator, denominator)

        # Возвращаем получившееся значение
        return num_div


