def fat(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

def n_binomial(n, p):
    return fat(n) // (fat(p) * fat(n - p))


print(n_binomial(0, 0))
print(n_binomial(1, 0), n_binomial(1, 1))
print(n_binomial(2, 0), n_binomial(2, 1), n_binomial(2, 2))
print(n_binomial(3, 0), n_binomial(3, 1), n_binomial(3, 2), n_binomial(3, 3))
print(n_binomial(4, 0), n_binomial(4, 1), n_binomial(4, 2), n_binomial(4, 3), n_binomial(4, 4))
print(n_binomial(5, 0), n_binomial(5, 1), n_binomial(5, 2), n_binomial(5, 3), n_binomial(5, 4), n_binomial(5, 5))
print(n_binomial(6, 0), n_binomial(6, 1), n_binomial(6, 2), n_binomial(6, 3), n_binomial(6, 4), n_binomial(6, 5), n_binomial(6, 6))
print(n_binomial(7, 0), n_binomial(7, 1), n_binomial(7, 2), n_binomial(7, 3), n_binomial(7, 4), n_binomial(7, 5), n_binomial(7, 6), n_binomial(7, 7))
print(n_binomial(8, 0), n_binomial(8, 1), n_binomial(8, 2), n_binomial(8, 3), n_binomial(8, 4), n_binomial(8, 5), n_binomial(8, 6), n_binomial(8, 7), n_binomial(8, 8))
print(n_binomial(9, 0), n_binomial(9, 1), n_binomial(9, 2), n_binomial(9, 3), n_binomial(9, 4), n_binomial(9, 5), n_binomial(9, 6), n_binomial(9, 7), n_binomial(9, 8), n_binomial(9, 9))
print(n_binomial(10, 0), n_binomial(10, 1), n_binomial(10, 2), n_binomial(10, 3), n_binomial(10, 4), n_binomial(10, 5), n_binomial(10, 6), n_binomial(10, 7), n_binomial(10, 8), n_binomial(10, 9), n_binomial(10, 10))