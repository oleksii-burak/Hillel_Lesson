import random


# Перша функція
def generate_2d_list(rows=None, cols=None):
    """
    Ця функція приймає два параметри: rows (кількість рядків)
    та cols (кількість стовпців).
    Якщо параметри не передані, вони встановлюються за замовчуванням у 5.
    Функція повертає двовимірний список, де кожен елемент
    є випадковим числом від 0 до 200.
    :param rows:
    :param cols:
    :return:
    """
    rows = rows or 5
    cols = cols or 5
    return [[random.randint(0, 200) for _ in range(cols)] for _ in range(rows)]


# Друга функція
def print_2d_table(table):
    """
    Ця функція приймає двовимірний список як параметр.
    Вона визначає максимальну довжину числа в списку
    для вирівнювання колонок.
    Потім вона друкує кожен рядок списку,
    вирівнюючи числа за правим краєм.
    :param table:
    :return:
    """
    max_width = max(len(str(num)) for row in table for num in row)
    for row in table:
        print(' '.join(str(num).rjust(max_width) for num in row))


# Виводимо трьох таблиць:
# Перша таблиця генерується без параметрів.
print("Табличка без параметрів:")
table1 = generate_2d_list()
print_2d_table(table1)

# Друга таблиця генерується з одним параметром (7 рядків).
print("\nТабличка з одним параметром:")
table2 = generate_2d_list(7)
print_2d_table(table2)

# Третя таблиця генерується з двома параметрами (4 рядки та 8 стовпців).
print("\nТабличка з двома параметрами:")
table3 = generate_2d_list(4, 8)
print_2d_table(table3)
