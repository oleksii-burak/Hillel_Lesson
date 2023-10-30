def check_sum_of_two_num(num_list1, target_sum1):
    """
    Функція перевіряє чи є у списку/послідовності 2 числа сума яких
    еквівалентна числу переданому 2-гим параметром. Функція повертає
    булеве значення як результат пошуку фукції.
    :param num_list1:
    :param target_sum1:
    :return:
    """
    seen = set()
    for num in num_list1:
        if target_sum1 - num in seen:
            return True
        seen.add(num)
    return False

# Створюємо список.
num_list1 = [1,1,1,1,1,1,1,1,5,1,1,1,19,2,2]
# Присвоюємо значення змінній.
target_sum1 = 24

# Виводимо значення.
print(check_sum_of_two_num(num_list1, target_sum1))