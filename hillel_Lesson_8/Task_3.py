import random

# Генеруємо множину з 15 випадкових чисел
numb_set = set()
while len(numb_set) < 15:
    numb_set.add(random.randint(1, 100))

# Обчислюємо суму парних та непарних чисел
evensum = sum(num for num in numb_set if num % 2 == 0)
oddsum = sum(num for num in numb_set if num % 2 != 0)

# Виводимо результат
print(numb_set)
if oddsum > evensum:
    print("Так")
else:
    print("Ні")
