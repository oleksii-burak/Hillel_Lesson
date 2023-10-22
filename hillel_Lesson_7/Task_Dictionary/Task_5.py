text0 = 'Python is good language to learn and in same time we like to tell that it is cool expereance for us'

# Створення словника з літер рядка як ключів та кількості їх входжень як значень
lettercount = {}

for lett in text0:
    # В цьому циклі ми перебираємо кожну літеру рядка
    if lett not in lettercount:
        # Якщо літери немає в словнику, ми додаємо її зі значенням 1.
        lettercount[lett] = 1
    # Якщо літера вже є в словнику, ми збільшуємо її значення на 1
    else:
        lettercount[lett] += 1

# Виведення результату
print(lettercount)
