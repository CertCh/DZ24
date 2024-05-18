def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(a, b):
    return sum(i for i in range(a, b + 1) if is_prime(i))

a = int(input("Введите начало интервала: "))
b = int(input("Введите конец интервала: "))
print(f"Сумма всех простых чисел в интервале от {a} до {b}: {sum_of_primes(a, b)}")
