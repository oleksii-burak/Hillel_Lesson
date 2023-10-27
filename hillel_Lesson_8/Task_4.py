data = [
 {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
 {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
 {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
 {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
 {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
 {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
]

# Створення множини робітників
work_set = {entry['name'] for entry in data}
print("Множина робітників:", work_set)

# Створення словника з сумою виторгу за тиждень для кожного працівника
sal_di = {}
for entry in data:
    if entry['name'] in sal_di:
        sal_di[entry['name']] += entry['price']
    else:
        sal_di[entry['name']] = entry['price']

print("Словник виторгу за тиждень:")
for work, totalsal in sal_di.items():
    print(f"{work}: {totalsal}")
