class ComplexNumber:
    """
    Класс для реализации комплексного числа.
    """

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
        Функция для проверки на равенство комплексных нескольких комплексных чисел.
        :param num_1: Первое комплексное число.
        :param num_2: Второе комплексное число.
        :param nums: Дополнительные комплексные числа.
        :return: Результат сравнения. True - если все введённые числа равны, False - в противном случае.
        """

        # Перебираем все введённые числа, проверяя, относятся ли они к классу ComplexNumber, и если не относятся,
        # то выбрасываем ошибку
        for num in [num_1, num_2, *nums]:
            if not(isinstance(num, ComplexNumber)):
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


