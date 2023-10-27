import random

# Генерація списку int_elements
int_elements = [random.randint(1, 500) for _ in range(25)]

# Список квадратів int_elements
int_elem_square = [x ** 2 for x in int_elements]

# Список остач ділення на 11 елементів int_elements
int_elem_mod = [x % 11 for x in int_elements]

# Список парних елементів int_elements
int_elem_coup = [coup for coup in int_elements if coup % 2 == 0]

# Список елементів int_elements з непарною кількістю цифр
int_elem_unpa = [unp for unp in int_elements if unp % 2 != 0]

# Список елементів int_elements, що стоять на позиціях які не є кратними 3
int_elem_not3 = [
    int_elements[i] for i in range(len(int_elements)) if (i+1) % 3 != 0
]

# Виводимо результат
print("Список int_elements:", int_elements)
print("Список квадратів:", int_elem_square)
print("Список остач ділення на 11:", int_elem_mod)
print("Список парних елементів:", int_elem_coup)
print("Список з непарною кількістю цифр:", int_elem_unpa)
print("Список на позиціях не кратних 3:", int_elem_not3)
