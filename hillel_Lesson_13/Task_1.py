class TriangleChecker:
    """
    Цей клас містить метод is_triangle(), який перевіряє,
    чи можна сформувати трикутник з трьох сторін.
    """

    @staticmethod
    def is_triangle(a, b, c):
        """
        Перевіряє, чи можна сформувати трикутник з трьох сторін.

        Параметри:
        a, b, c (int/float): Довжини сторін, які потрібно перевірити.

        Повертає:
        str: Результат перевірки.
        """
        if any(type(side) not in [int, float] or side <= 0 for side in
               [a, b, c]):
            return "Потрібно вводити тільки позитивні числа!"
        if a + b > c and a + c > b and b + c > a:
            return "Ура, можна побудувати трикутник!"
        return "Жаль, але з цього трикутник не зробити."


class Triangle:
    """
    Цей клас є базовим класом для трикутників і може містити
    додаткові властивості або методи, специфічні для трикутників.
    """

    def __init__(self, a, b, c):
        """
        Ініціалізує трикутник з заданими сторонами.

        Параметри:
        a, b, c (int/float): Довжини сторін трикутника.
        """
        self.a = a
        self.b = b
        self.c = c


class ExtTriangle(Triangle, TriangleChecker):
    """
    Цей клас успадковує властивості від Triangle та TriangleChecker.
    Він використовує метод is_triangle() для перевірки,
    чи можливо сформувати трикутник з заданих сторін.
    """

    def __init__(self, a, b, c):
        """
        Ініціалізує розширений трикутник з заданими сторонами.

        Параметри:
        a, b, c (int/float): Довжини сторін трикутника.
        """
        super().__init__(a, b, c)

    def is_triangle(self):
        """
        Використовує метод is_triangle() з TriangleChecker для перевірки,
        чи можливо сформувати трикутник зі сторін екземпляра.

        Повертає:
        str: Результат перевірки.
        """
        return TriangleChecker.is_triangle(self.a, self.b, self.c)


# Перевірка
examples = [
    (3, 4, 5),  # Можна побудувати трикутник
    (-3, 4, 5),  # Негативні числа
    ("3", 4, 5),  # Не числа
    (1, 2, 3)  # Не можна побудувати трикутник
]

for sides in examples:
    triangle = ExtTriangle(*sides)
    print(triangle.is_triangle())
