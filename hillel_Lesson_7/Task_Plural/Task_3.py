# Тестовий список з різними типами даних
test_list = [1, 2, 3, [4, 5], {2, 4, 5, 2}, {'key': 'value'}, 'string', 6, (7, 8), ["ds", "ds"]]
# Створюэмо множину.
set_list = set()

# Ітеруємо список.
for setli in test_list:

    # Перевіряємо щоб все що додається до множини відповідало потребам
    if not type(setli) == list and not type(setli) == dict and not type(setli) == set:
        set_list.add(setli)

# Виводимо результат.
print(set_list)
