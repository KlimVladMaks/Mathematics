class ComplexNumber:
    """
    Класс для реализации комплексного числа.
    """

    # TODO: Решить проблему, что при изменении re_z и im_z, pair_form остаётся прежней
    def __init__(self, re_z: int = 0, im_z: int = 0):
        """
        Инициализируем комплексное число при создании экземпляра класса.
        :param re_z: Вещественная часть числа.
        :param im_z: Мнимая часть числа.
        """

        # Проверяем, что введены числовые коэффициенты, и если это не так, то выбрасываем ошибку
        if (type(re_z) is not int) or (type(im_z) is not int):
            raise Exception("Введены нечисловые коэффициенты для комплексного числа")

        # Задаём вещественную и мнимую часть комплексного числа
        self.re_z = re_z
        self.im_z = im_z

        # Задаём вид комплексного числа в формате пары чисел
        self.pair_form = (re_z, im_z)

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

        # Создаём нулевые переменные для вещественной и мнимой части
        re_z = 0
        im_z = 0

        # Перебираем все переданные числа, складывая их вещественные и мнимые части с созданными выше
        for num in [num_1, num_2, *nums]:
            re_z += num.re_z
            im_z += num.im_z

        # Возвращаем комплексное число с вещественной и мнимой частями, полученными в результате сложения
        return ComplexNumber(re_z, im_z)

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




