import random

# Запитуємо розмір матриці у користувача
n0 = int(input("Введіть розмір матриці n: "))

# Генеруємо матрицю
matrix = [[random.randint(10, 99) for _ in range(n0)] for _ in range(n0)]

# Виводимо матрицю
for row in matrix:
    print(row)

# Обчислюємо суму чисел по діагоналі
diagsum = sum(matrix[i][i] for i in range(n0))
print("Сума чисел по діагоналі:", diagsum)

# Обчислюємо суму чисел останнього стовбця
lastcolsum = sum(row[-1] for row in matrix)
print("Сума чисел останнього стовбця:", lastcolsum)
