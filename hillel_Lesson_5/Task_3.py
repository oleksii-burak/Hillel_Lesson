print("Треба ввести ціле число, якщо введете 0 то программа почне рахувати.")

# Створюємо змінні з списком та змінні в які будемо добавляти значення.
form0 = []
par = 0
nepar = 0

# Тут ми прсимо ввести числа та добавляємо числа в список, такоже
# робтмо перевірку на введення 0 для того чоб программа почала
# рахувати, також  робимо перевірку щоб вводились тільки цифри.
while True:
    numinput = input("Введіть число:")
    if numinput.isdigit():
        numint = int(numinput)
        if numint == 0:
            break
        form0.append(numint)

    else:
        if not numinput:
            print("Ви не ввели число!")

        else:
            print("Ви ввели не коректний символ!",
                  "Перевірте та введіть корректно:", sep = "\n"
                  )

# Підраховуємо парні та не парні числа.
for num1 in form0:
    if num1 % 2 == 0:
        par += 1
    else:
        nepar += 1

# Визначає мосереднє арифметичне усіх введених чисел.
vellen = len(form0)
result1 = sum(form0)
result2 = result1 // vellen

# Дізнаємося саме максимальне та мінімальне число.
result3 = max(form0)
result4 = min(form0)

# Перехідні змінні на результат про кількість парних та не парних чисел
result5 = par
result6 = nepar


# Виводимо результати
print("+-------------Ваш результат!-------------+")
print(f"Сума чисел: {result1}")
print(f"Середнє арифметичне: {result2}")
print(f"Максимальне значення: {result3}")
print(f"Мінімальне значення: {result4}")
print(f"Кількість парних чисел: {result5}")
print(f"Кількість непарних чисел: {result6}")
