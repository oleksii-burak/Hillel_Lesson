import random

def sortmatrix(matrix):
    """
    Функція для сортування матриці за заданими умовами.
    Спочатку сортує стовпці за сумою їх елементів, потім сортує елементи в кожному стовпці.
    """
    M = len(matrix)  # Зберігаємо розмір матриці

    # Сортування стовпців за сумою елементів
    for i in range(M):
        for j in range(M-1):
            # Порівнюємо суми сусідніх стовпців
            if sum(matrix[k][j] for k in range(M)) > sum(matrix[k][j+1] for k in range(M)):
                # Міняємо місцями стовпці
                for k in range(M):
                    matrix[k][j], matrix[k][j+1] = matrix[k][j+1], matrix[k][j]


    # Сортування елементів у стовпцях
    for j in range(M):
        for i in range(M):
            for k in range(M-i-1):
                # Умова сортування залежить від парності стовпця
                if (j % 2 == 0 and matrix[k][j] > matrix[k+1][j]) or (j % 2 != 0 and matrix[k][j] < matrix[k+1][j]):
                    # Міняємо місцями елементи
                    matrix[k][j], matrix[k+1][j] = matrix[k+1][j], matrix[k][j]


def printmatrix(matrix):
    """
    Функція для виведення матриці на екран.
    Виводить матрицю та суму елементів кожного стовпця.
    """
    M = len(matrix)  # Зберігаємо розмір матриці
    for row in matrix:
        for item in row:
            print(f"{item:3}", end=" ")  # Вивід елементів рядка
        print()
    for j in range(M):
        print(f"{sum(matrix[i][j] for i in range(M)):3}", end=" ")  # Вивід суми елементів стовпця
    print()


# Генерація матриці
M = int(input("Введіть розмір матриці (більше 5): "))
matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]

print("До сортування:")
printmatrix(matrix)

sortmatrix(matrix)

print("Після сортування:")
printmatrix(matrix)
