import random

# Створюємо списки.
list1 = []
list2 = []

# Додаємо рандомні числа в списки.
for i in range(1, random.randint(20, 30)):
    list1.append(random.randint(1, 50))

for i in range(1, random.randint(20, 30)):
    list2.append(random.randint(1, 50))

# Використовуємо множини для визначення унікальних чисел у списках.
uniqlist1 = set(list1)
uniqlist2 = set(list2)

# Знаходимо перетин двох множин, що представляє числа,
# які містяться в обох списках.
result = uniqlist1.intersection(uniqlist2)

# Виводимо всі числа які містяться в списках.
print(f"Числа які містить перший список: {list1}")
print(f"Числа які містить другий список: {list2}")

# Виводимо кількість спільних унікальних чисел
print(f"У обох списках міститься {len(result)} різних чисел.")
