def is_prime(num):
    """Перевіряє, чи є число простим."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n, z):
    """Генератор простих чисел у діапазоні від n до z."""
    for num in range(n, z + 1):
        if is_prime(num):
            yield num

# Використання генератора
n = 10  # Початок діапазону
z = 50  # Кінець діапазону

primes = generate_primes(n, z)
print(*primes)
