def input_and_process():
    try:
        # Запитуємо введення двох значень
        value1 = input("Введіть перше значення: ")
        value2 = input("Введіть друге значення: ")

        # Спробуємо перетворити ці значення на числа
        num1 = float(value1)
        num2 = float(value2)

        # Якщо обидва значення є числами, сумуємо їх
        return num1 + num2
    except ValueError:
        # Якщо хоча б одне зі значень не є числом, виконуємо конкатенацію
        return value1 + value2

# Викликаємо функцію
result = input_and_process()
print("Результат: ", result)
