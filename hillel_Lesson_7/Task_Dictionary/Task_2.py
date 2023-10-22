import random

# Створення словника з 20 випадковими числовими значеннями
dictionary1 = {}
for num in range(1, 21):
    velnum = random.randint(1, 100)
    dictionary1[f"Num_{num}"] = velnum

# Перемноження всіх значень словника
result = 1
for value in dictionary1.values():
    result *= value

# Виводимо результат.
print("Сгенерований словник:", dictionary1)
print("Результат множення чисел:", result)
