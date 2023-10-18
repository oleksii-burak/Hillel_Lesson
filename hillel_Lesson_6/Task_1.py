# Запитуємо суму кредиту в клієнта
loan_amount = float(input("Введіть суму кредиту: "))

# Присвоюємо змінній значення котре буде застосовуватися для розділу.
rasdel = "-+-" * 10

# Дізнаємося чисту що місячну сумму для сплати.
loan_amount12 = loan_amount
resvel12 = loan_amount / 12
resvel60 = loan_amount / 60

# Тут ми будемо зберігати загальну суму з відсотками.
total_payment12 = 0
total_payment60 = 0
month1 = 1
month2 = 1

# Цикл для розрахунку платежів за кожний місяць на протязі одного року.
for month0 in range(1, 13):
    # Дізнаємось суму відсотку.
    monthly_payment12 = (2 / 100) * loan_amount12
    # Додаємо суму відсотку до суми платежу та доаємо до загального заначення.
    total_payment12 += resvel12 + monthly_payment12

    # Виводимо щомісячний платіж з врахуванням відсотків та відсотки окремо.
    print(f"Місяць {str(month1).rjust(3)}: {resvel12 + monthly_payment12:.2f}",
        f"(Проценти: {monthly_payment12:.2f})")

    # Дізнаємося залишок суми для виплати за кожен місяць.
    loan_amount12 -= resvel12
    month1 += 1

# Виводимо роздиляючий рядок та загальний результат.
print(rasdel)
print(f"Загальна сума сплати: {total_payment12:.2f}")

# Цикл для розрахунку платежів за кожний місяць на протязі п'яти років
print("", "", sep="\n")
for month in range(1, 61):
    # Дізнаємось суму відсотку та в заленості від кількості місяців
    # підставляємо потрібний відсоток.
    if month >= 24:
        monthly_payment60 = (4 / 100) * loan_amount
    else:
        monthly_payment60 = (2 / 100) * loan_amount

    # Додаємо суму відсотку до суми платежу та доаємо до загального заначення.
    total_payment60 += resvel60 + monthly_payment60
    # Виводимо щомісячний платіж з врахуванням відсотків та відсотки окремо.
    print(
        f"Місяць {str(month2).rjust(3)}: {resvel60 + monthly_payment60:.2f}",
        f"(Проценти: {monthly_payment60:.2f})"
    )
    # Дізнаємося залишок суми для виплати за кожен місяць.
    loan_amount -= resvel60
    month2 += 1

# Виводимо роздиляючий рядок та загальний результат
print(rasdel)
print(f"Загальна сума сплати: {total_payment60:.2f}")

