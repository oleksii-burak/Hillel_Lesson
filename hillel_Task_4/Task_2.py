# Завдання A
# Створюємо кортежі
first = (1, 2, 3, 4, 5)
second = (5, 6, 7, 8, 9)

# Конвертуємо кортежі в список
result = list(first + second)

# Виводимо результат
print(result)

# Завдання B
# Додаємо кртежі та список в один кортеж
t_result = (result, first[::-1], second[::-1])

# Виводимо результат
print(t_result)

# Завдання C

# Створюємо змінні в яким присвоюємо індекси з змістом з кортежу t_result
t_result1 = t_result[0]
t_result2 = t_result[1]
t_result3 = t_result[2]

# Тут виводимо результат в якому покаже зміст по заданному індексу
print(t_result1[2])
print(t_result2[2])
print(t_result3[2])
