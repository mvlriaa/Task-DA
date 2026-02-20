def prime_factors(n):
    """Возвращает список простых множителей натурального числа n"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def prime_factor_optim(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
    if n > 1:
        factors.append(n)

    return factors

n = 987654321987654321
print(prime_factors(n))
print(prime_factor_optim(n))
