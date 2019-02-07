def regular_modulus_exp(x, n, d):
    return x ** n % d

def fast_modulus_exp(x, n, d):
    if d == 1:
        return 0
    result = 1
    x %= d
    while n > 0:
        if n % 2 == 1:
            result = (result * x) % d
        n = (n >> 1)
        x = (x * x) % d
    return result