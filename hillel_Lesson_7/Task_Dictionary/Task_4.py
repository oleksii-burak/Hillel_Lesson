import random

# Створюємо списки та словник
list1 = []
list2 = []
dict0 = {}

# Присваюємо змінній значення
range1 = 1

# Додаєммо значення в списки
for q in range(1, 21):
    velnum1 = random.randint(1, 100)
    list1.append(velnum1)

for w in range(1, 21):
    velnum2 = random.randint(1, 100)
    list2.append(velnum2)

# Беремо значення з списків та в потрібній формі додаємо до словника
for e in list1:
    # Тут ми достаємо потрібний результат зі списку
    for r in range(range1, 21):
        velres = list2[range1 - 1]
        range1 += 1
        break
    # Тут ми результат зі списку 1 додаємо як ключ а результат
    # зі списку 2 додаємо як результат до словника
    dict0[e] = velres

# Виводимо результат
print(list1)
print(list2)
print(dict0)

