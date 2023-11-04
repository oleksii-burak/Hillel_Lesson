import math  # Математичний модуль для обчислень

# Лямбда-функція для обчислення гіпотенузи
hypot = lambda x, y=1: math.sqrt(x**2 + y**2)

# Ініціалізація списків
list1 = []
list2 = []

# Заповнення list1
for xv in range(1, 4):
    if xv == 1:
        print("Варіант 1.")
    vel1 = input(f"Введіть {xv} число:")
    if vel1.isdigit():
        list1.append(int(vel1))
    else:
        print("Невірний символ!")

# Заповнення list2
for xv in range(1, 4):
    if xv == 1:
        print("Варіант 2.")
    vel2 = input(f"Введіть {xv} число:")
    if vel2.isdigit():
        list2.append(int(vel2))
    else:
        print("Невірний символ!")

# Обчислення результатів
result1 = list(map(hypot, list1))
result2 = list(map(hypot, list1, list2))

# Виведення результатів
print(result1)
print(result2)

