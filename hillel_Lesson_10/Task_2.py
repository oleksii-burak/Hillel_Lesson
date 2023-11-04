def is_prime(num):
    """Перевіряє, чи є число простим."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(nn, zz):
    """Генератор простих чисел у діапазоні від n до z."""
    for num in range(nn, zz + 1):
        if is_prime(num):
            yield num


# Використання генератора
nn = 10  # Початок діапазону
zz = 50  # Кінець діапазону

primes = generate_primes(nn, zz)
print(*primes)
