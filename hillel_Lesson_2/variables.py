# Заміна значень 2х змінних використовючи 3-тю змінну
vel1 = 15
vel2 = 30

vel3 = vel2
vel2 = vel1
vel1 = vel3

print(vel1)
print(vel2)

# заміна значень 2х змінних використовуючи властивості python
vel1 = 15
vel2 = 30

vel1, vel2 = vel2, vel1

print(vel1)
print(vel2)

# заміна значень 2 змінних не використівуючи 2х попредніх варіантів.
vel1 = 15
vel2 = 33

vel1 = vel1 ^ vel2
vel2 = vel1 ^ vel2
vel1 = vel1 ^ vel2

print(vel1)
print(vel2)
