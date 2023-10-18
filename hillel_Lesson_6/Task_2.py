# Запитуэмо число.
n = int(input("Введіть кількість рядків: "))

# Призначаємо змінні
qwe = "1"
iw0 = 1
nlen = len(str(n))

# Створюємо цикл.
for iw in range(1, n + 1):
    # Призначаємо змінну
    qwe0 = "0"
    # Виводимо результат по заданним параметрам
    print(str(iw0).rjust(nlen), qwe.rjust(n), sep=" ")
    qwe += qwe0
    iw0 += 1